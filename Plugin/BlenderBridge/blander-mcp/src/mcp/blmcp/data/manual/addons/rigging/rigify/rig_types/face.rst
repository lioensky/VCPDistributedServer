
****
Face
****

These rig types implement components of a modular face.


.. _rigify.rigs.face.basic_tongue:

face.basic_tongue
=================

Generates a simple tongue, extracted from the original PitchiPoy :ref:`super_face <rigify.rigs.faces.super_face>` rig.

B-Bone Segments (integer)
   Defines the number of b-bone segments each tweak control will be split into.
Primary Control Layers
   Optionally specifies bone collections for the main control.


.. _rigify.rigs.face.skin_eye:

face.skin_eye
=============

Implements a skin system :ref:`parent controller <rigify.rigs.skin.skin_parents>` that manages
two skin chains for the top and bottom eyelids in addition to generating the eye rotation mechanism.

The rig must have two child skin chains with names tagged with ``.T`` and ``.B`` symmetry
to mark the top and bottom eyelid, which are connected at their ends forming eye corners.
The chains are rigged to follow the surface of the eye and twist to its normal.

In addition, it creates target controls for aiming the eye, including a master control shared by
all eyes under the same parent rig. The eyelids are rigged to follow the movement of the eyeball
with adjustable influence.

Eyeball and Iris Deforms
   Generates deform bones for the eyeball and the iris, the latter copying XZ scale from
   the eye target control. The iris is located at the tail of the ORG bone.
Eyelid Detach Option
   Generates a slider to disable the mechanism that keeps eyelid controls stuck to the surface of the eye.
Split Eyelid Follow Slider
   Generates two separate sliders for controlling the influence of the eye rotation on X and Z eyelid motion.
Eyelids Follow Default
   Depending on *Split Eyelid Follow Slider*, specifies the default values for the split follow sliders,
   or fixed factors to be multiplied with the single common follow influence slider value.


.. _rigify.rigs.face.skin_jaw:

face.skin_jaw
=============

Implements a skin system :ref:`parent controller <rigify.rigs.skin.skin_parents>` that manages
one or more loops of mouth skin chains in response to the movement of jaw and mouth controls.

The rig must have one or more child chain loops, each formed by four skin chains tagged
with ``.T``/``.B`` and ``.L``/``.R`` symmetrical names.

The lip loops are sorted into layers based on the distance from corners to the common
center and rigged with blended influence of the jaw and the master mouth control.
Other child rigs become children of the jaw.

Bottom Lip Influence
   Specifies the influence of the jaw on the inner bottom lip with mouth lock disabled.
Locked Influence
   Specifies the influence of the jaw on both lips of locked mouth.
Secondary Influence Falloff
   Specifies the factor by which influence fades away with each successive lip loop
   (for bottom lip loops the blend moves away from inner bottom lip to full jaw influence).
