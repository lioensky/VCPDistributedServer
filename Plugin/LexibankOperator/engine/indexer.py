#!/usr/bin/env python3
import os, sys, io, csv, json, time, zipfile, sqlite3, hashlib
from pathlib import Path

def get_fingerprint(cldf_dir: Path) -> str:
    h = hashlib.sha256()
    for name in ["wordlist-metadata.json", "concepts.csv", "languages.csv", "forms.csv.zip"]:
        p = cldf_dir / name
        if p.exists():
            st = p.stat()
            h.update(f"{name}:{st.st_size}:{st.st_mtime}".encode("utf-8"))
    return h.hexdigest()[:16]

def build(upstream: Path, data_dir: Path, force=False):
    data_dir.mkdir(parents=True, exist_ok=True)
    fp = get_fingerprint(upstream)
    target_db = data_dir / f"lexibank_{fp}.sqlite"
    link_db = data_dir / "current.sqlite"

    if target_db.exists() and not force:
        update_link(data_dir, target_db.name, fp, upstream)
        print(json.dumps({"status": "cached", "version": fp, "db": str(target_db)}, ensure_ascii=False))
        return

    tmp_db = data_dir / f"build_{fp}.tmp.sqlite"
    if tmp_db.exists(): tmp_db.unlink()

    conn = sqlite3.connect(tmp_db)
    cur = conn.cursor()
    cur.execute("PRAGMA synchronous = 0;")
    cur.execute("PRAGMA journal_mode = OFF;")

    cur.execute("CREATE TABLE languages (id TEXT PRIMARY KEY, name TEXT, macroarea TEXT, latitude REAL, longitude REAL, glottocode TEXT, iso TEXT, family TEXT, subgroup TEXT);")
    cur.execute("CREATE TABLE concepts (id TEXT PRIMARY KEY, name TEXT, concepticon_id TEXT, gloss TEXT, core TEXT);")
    cur.execute("CREATE TABLE forms (id TEXT PRIMARY KEY, language_id TEXT, parameter_id TEXT, form TEXT, value TEXT, segments TEXT, cognacy TEXT, loan INT, cv TEXT, sca TEXT);")

    # Languages
    p_lang = upstream / "languages.csv"
    if p_lang.exists():
        with open(p_lang, "r", encoding="utf-8") as f:
            rows = [(r.get("ID",""), r.get("Name",""), r.get("Macroarea",""),
                     float(r["Latitude"]) if r.get("Latitude") else None,
                     float(r["Longitude"]) if r.get("Longitude") else None,
                     r.get("Glottocode",""), r.get("ISO639P3code",""),
                     r.get("Family",""), r.get("Subgroup","")) for r in csv.DictReader(f)]
            cur.executemany("INSERT INTO languages VALUES (?,?,?,?,?,?,?,?,?);", rows)
        conn.commit()

    # Concepts
    p_con = upstream / "concepts.csv"
    if p_con.exists():
        with open(p_con, "r", encoding="utf-8") as f:
            rows = [(r.get("ID",""), r.get("Name",""), r.get("Concepticon_ID",""),
                     r.get("Concepticon_Gloss",""), r.get("Core_Concept","")) for r in csv.DictReader(f)]
            cur.executemany("INSERT INTO concepts VALUES (?,?,?,?,?);", rows)
        conn.commit()

    # Forms
    p_zip = upstream / "forms.csv.zip"
    p_raw = upstream / "forms.csv"
    stream, zf = None, None
    if p_zip.exists():
        zf = zipfile.ZipFile(p_zip, "r")
        name = "forms.csv" if "forms.csv" in zf.namelist() else [n for n in zf.namelist() if n.endswith("forms.csv")][0]
        stream = io.TextIOWrapper(zf.open(name), encoding="utf-8")
    elif p_raw.exists():
        stream = open(p_raw, "r", encoding="utf-8")

    if stream:
        reader = csv.DictReader(stream)
        batch = []
        for r in reader:
            batch.append((r.get("ID",""), r.get("Language_ID",""), r.get("Parameter_ID",""),
                          r.get("Form",""), r.get("Value",""), r.get("Segments",""),
                          r.get("Cognacy",""), 1 if r.get("Loan","").lower() in ("true","1") else 0,
                          r.get("CV_Template",""), r.get("SCA_Sound_Classes","")))
            if len(batch) >= 40000:
                cur.executemany("INSERT INTO forms VALUES (?,?,?,?,?,?,?,?,?,?);", batch)
                batch.clear()
        if batch:
            cur.executemany("INSERT INTO forms VALUES (?,?,?,?,?,?,?,?,?,?);", batch)
        conn.commit()
        if zf: zf.close()
        else: stream.close()

    # Indexes
    cur.execute("CREATE INDEX idx_forms_param ON forms(parameter_id);")
    cur.execute("CREATE INDEX idx_forms_lang ON forms(language_id);")
    cur.execute("CREATE INDEX idx_forms_form ON forms(form);")
    cur.execute("CREATE INDEX idx_concepts_gloss ON concepts(gloss);")
    cur.execute("CREATE INDEX idx_lang_glotto ON languages(glottocode);")
    cur.execute("CREATE INDEX idx_lang_family ON languages(family);")
    conn.commit()
    conn.close()

    tmp_db.rename(target_db)
    update_link(data_dir, target_db.name, fp, upstream)
    print(json.dumps({"status": "success", "version": fp, "db": str(target_db)}, ensure_ascii=False))

def update_link(data_dir: Path, target_name: str, fp: str, upstream: Path):
    cur_link = data_dir / "current.sqlite"
    if cur_link.is_symlink() or cur_link.exists(): cur_link.unlink()
    try:
        cur_link.symlink_to(target_name)
    except OSError:
        import shutil
        shutil.copy2(data_dir / target_name, cur_link)
    with open(data_dir / "state.json", "w", encoding="utf-8") as f:
        json.dump({"active_version": fp, "upstream": str(upstream), "db": target_name, "time": time.ctime()}, f, ensure_ascii=False)

if __name__ == "__main__":
    up = os.environ.get("UPSTREAM_CLDF_DIR", str(Path(__file__).resolve().parent.parent.parent / "lexibank-analysed" / "cldf"))
    data = os.environ.get("DATA_DIR", str(Path(__file__).resolve().parent.parent / "data"))
    force = "--force" in sys.argv
    build(Path(up), Path(data), force)