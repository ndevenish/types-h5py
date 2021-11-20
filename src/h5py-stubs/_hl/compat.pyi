from os import fsdecode as fsdecode
from os import fsencode as fsencode
from os import fspath as fspath
from typing import Any

from ..version import hdf5_built_version_tuple

WINDOWS_ENCODING: Any

def filename_encode(filename): ...
def filename_decode(filename): ...
