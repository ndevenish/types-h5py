set -euxo pipefail

stubgen -p h5py
# Replace cython_function_or_method
find out -name "*.pyi" -print0 | xargs  -0 sed -E -i '' -e 's;^([^ ]+) *: *cython_function_or_method;def \1(*args, **kwargs) -> Any: ...;g'
# Fix cython properties
# find out -name "*.pyi" -print0 | xargs  -0 sed -E -i '' \
#     -e 's;( +)([^ :]+): ClassVar\[getset_descriptor\] = ...;\1@property\n\1def \2(self) -> Any: ...\n\1@\2.setter\n\1def \2(self, value) -> None: ...;g'
# Just declare cython properties as instance variables
find out -name "*.pyi" -print0 | xargs  -0 sed -E -i '' \
    -e 's;( +)([^ :]+): ClassVar\[getset_descriptor\] = ...;\1\2 : Any;g'

# Strip pyx vtable
find out -name "*.pyi" -print0 | xargs  -0 sed -E -i '' \
    -e 's;__pyx_vtable__: ClassVar\[PyCapsule\] = ...;;g'

# Repeat import names 'from a import b as b'
# NOTE: This breaks explicit re-export. Things we need to do this for are handled later
find out -name "*.pyi" | grep -v "__init__.pyi" | xargs perl -p -i -e 's;(?<=[ ,])([a-zA-Z][^,\s]*) as \1;\1;g'
# Remove __pyx_unpickle
find out -name "*.pyi" -print0 | xargs -0 perl -p -i -e 's;^def __pyx.+\n;;g' out/h5py/_conv.pyi
# np.object_
find out -name "*.pyi" -print0 | xargs -0 perl -p -i -e 's;\[object_\];\[numpy.object_\];g' out/h5py/_conv.pyi
# Handle explicit re-exports
sed -i '' -e '1s/^/from os import fsdecode as fsdecode, fsencode as fsencode, fspath as fspath\n/' out/h5py/_hl/compat.pyi
sed -i '' -e 's/with_phil/with_phil as with_phil/' -e 's/ phil/ phil as phil/' out/h5py/_hl/base.pyi
# classmethod __init__
# find out -name "*.pyi" -print0 | xargs -0 sed -E -i '' 'N; s/@classmethod\n +def __init__/def __init__/g'
# find $PWD -type d | while read dir;do find $dir -type f -maxdepth 1 | head -1;done

# Rewrite classmethod __init__ definitions
cat <<EOF > rewrite.py
import re
import sys
from pathlib import Path
import difflib

for filename in sys.argv[3:]:
    p = Path(filename)
    print("Rewriting", p)
    in_s = p.read_text()
    out_s = re.sub(sys.argv[1], sys.argv[2], in_s, flags=re.M)
    if out_s != in_s:
        print(
            "\n".join(
                difflib.unified_diff(
                    in_s.splitlines(),
                    out_s.splitlines(),
                    fromfile=filename,
                    tofile=filename,
                )
            )
        )
        p.write_text(out_s)
        print()
EOF

find out -name "*.pyi" -print0 | xargs -0 python3 rewrite.py \
    '@classmethod\n\s+def __init__' 'def __init__'

# Format and sort this
isort out
black out

# Now apply custom patches

# NamedTuples - patching python include blocks is unstable because no context.
# So do the header parts separately.
sed -i '' -e '1s/^/from typing import NamedTuple\n/' out/h5py/h5d.pyi
sed -i '' -e 's/import _collections//g' out/h5py/h5d.pyi
sed -i '' -e 's/import _collections//g' out/h5py/h5t.pyi
sed -i '' -e '1s/^/from typing import NamedTuple\n/' out/h5py/h5t.pyi
# exit
patch -p1 < 0001-Fix-NamedTuples.patch

# Re-Format and sort this
isort out
black out


