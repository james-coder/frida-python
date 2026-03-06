import sys
from pathlib import Path

# Allow loading the compiled extension from Meson build paths that provide
# "frida/_frida/_frida.*" alongside this source package path.
for entry in sys.path:
    candidate = Path(entry) / "frida" / "_frida"
    if candidate.is_dir():
        candidate_path = str(candidate)
        if candidate_path not in __path__:
            __path__.append(candidate_path)

from . import _frida as _backend

for name in dir(_backend):
    if name == "__version__" or not name.startswith("__"):
        globals()[name] = getattr(_backend, name)
