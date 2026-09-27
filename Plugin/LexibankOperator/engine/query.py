#!/usr/bin/env python3
import os, sys, json, sqlite3
from pathlib import Path

def get_db_path():
    base_dir = Path(__file__).resolve().parent.parent
    data_raw = os.environ.get("DATA_DIR", "./data")
    data_dir = Path(data_raw) if Path(data_raw).is_absolute() else (base_dir / data_raw).resolve()
    db_file = data_dir / "current.sqlite"
    if not db_file.exists():
        state_file = data_dir / "state.json"
        if state_file.exists():
            with open(state_file, "r", encoding="utf-8") as f:
                st = json.load(f)
                cand = data_dir / st.get("db", "")
                if cand.exists(): return cand
        return None
    return db_file

def query_concept(conn, gloss, family=None, limit=50):
    cur = conn.cursor()
    sql = """
    SELECT f.form, f.value, f.segments, f.cognacy, f.loan,
           l.name as lang_name, l.family, l.glottocode,
           c.gloss, c.name as concept_name
    FROM forms f
    JOIN concepts c ON f.parameter_id = c.id
    JOIN languages l ON f.language_id = l.id
    WHERE (c.gloss LIKE ? OR c.name LIKE ?)
    """
    params = [f"%{gloss}%", f"%{gloss}%"]
    if family:
        sql += " AND l.family LIKE ?"
        params.append(f"%{family}%")
    sql += " LIMIT ?"
    params.append(limit)
    cur.execute(sql, params)
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]

def query_cognate(conn, word, limit=50):
    cur = conn.cursor()
    sql = """
    SELECT f.form, f.value, f.segments, f.cognacy,
           l.name as lang_name, l.family, l.glottocode,
           c.gloss
    FROM forms f
    JOIN concepts c ON f.parameter_id = c.id
    JOIN languages l ON f.language_id = l.id
    WHERE f.form = ? OR f.value = ?
    LIMIT ?
    """
    cur.execute(sql, (word, word, limit))
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]

def query_lang(conn, code):
    cur = conn.cursor()
    sql = "SELECT * FROM languages WHERE id = ? OR glottocode = ? OR iso = ? OR name LIKE ? LIMIT 1"
    cur.execute(sql, (code, code, code, f"%{code}%"))
    row = cur.fetchone()
    if not row: return None
    cols = [d[0] for d in cur.description]
    lang = dict(zip(cols, row))
    cur.execute("SELECT count(*) FROM forms WHERE language_id = ?", (lang["id"],))
    lang["total_forms"] = cur.fetchone()[0]
    return lang

def get_status(conn):
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM languages;")
    n_langs = cur.fetchone()[0]
    cur.execute("SELECT count(*) FROM concepts;")
    n_concepts = cur.fetchone()[0]
    cur.execute("SELECT count(*) FROM forms;")
    n_forms = cur.fetchone()[0]
    return {"languages": n_langs, "concepts": n_concepts, "forms": n_forms}

def extract_str(val):
    if isinstance(val, str):
        return val.strip()
    if isinstance(val, dict):
        for k in ["command", "action", "cmd", "name", "value"]:
            if k in val and isinstance(val[k], str):
                return val[k].strip()
    return ""

def main():
    try:
        raw_in = sys.stdin.read()
        req = json.loads(raw_in) if raw_in.strip() else {}
    except Exception as e:
        print(json.dumps({"error": f"Invalid JSON stdin: {e}"}, ensure_ascii=False))
        return

    # 全格式解构：处理 command 可能是 string 也可能是 dict 的情况
    raw_cmd = req.get("command") or req.get("action") or req.get("cmd") or ""
    cmd = extract_str(raw_cmd).lower()

    if not cmd and isinstance(req.get("args"), dict):
        cmd = extract_str(req["args"].get("command")).lower()

    if cmd == "sync":
        import subprocess
        indexer_script = Path(__file__).resolve().parent / "indexer.py"
        cmd_args = [sys.executable, str(indexer_script)]
        force = req.get("force")
        if force is True or str(force).lower() in ("true", "1"):
            cmd_args.append("--force")
        res = subprocess.run(cmd_args, capture_output=True, text=True)
        try:
            out = json.loads(res.stdout.strip())
            print(json.dumps(out, ensure_ascii=False))
        except Exception:
            print(json.dumps({"output": res.stdout, "stderr": res.stderr, "exit_code": res.returncode}, ensure_ascii=False))
        return

    db_path = get_db_path()
    if not db_path or not db_path.exists():
        print(json.dumps({"error": f"数据库尚未建立（解析到命令: '{cmd}'），请先调用 sync 命令生成索引。"}, ensure_ascii=False))
        return

    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)

    if cmd == "concept_lookup":
        gloss = req.get("concept") or req.get("gloss") or ""
        if isinstance(gloss, dict): gloss = extract_str(gloss)
        family = req.get("family")
        if isinstance(family, dict): family = extract_str(family)
        limit = int(req.get("limit", 50))
        results = query_concept(conn, str(gloss), str(family) if family else None, limit)
        print(json.dumps({"concept": gloss, "count": len(results), "results": results}, ensure_ascii=False))
    elif cmd == "cognate_trace":
        word = req.get("word", "")
        if isinstance(word, dict): word = extract_str(word)
        limit = int(req.get("limit", 50))
        results = query_cognate(conn, str(word), limit)
        print(json.dumps({"word": word, "count": len(results), "results": results}, ensure_ascii=False))
    elif cmd == "lang_profile":
        code = req.get("code") or req.get("lang") or ""
        if isinstance(code, dict): code = extract_str(code)
        lang = query_lang(conn, str(code))
        print(json.dumps({"profile": lang}, ensure_ascii=False))
    elif cmd == "status":
        st = get_status(conn)
        state_file = Path(db_path).parent / "state.json"
        meta = {}
        if state_file.exists():
            with open(state_file, "r", encoding="utf-8") as f:
                meta = json.load(f)
        st["meta"] = meta
        st["db_path"] = str(db_path)
        print(json.dumps(st, ensure_ascii=False))
    else:
        print(json.dumps({"error": f"Unknown command: '{cmd}'", "received_payload": req}, ensure_ascii=False))

    conn.close()

if __name__ == "__main__":
    main()