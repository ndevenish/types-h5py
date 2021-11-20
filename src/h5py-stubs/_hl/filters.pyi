from collections.abc import Mapping
from typing import Any

from .. import h5d, h5f, h5p, h5z
from .compat import filename_encode

DEFAULT_GZIP: int
DEFAULT_SZIP: Any
decode: Any
encode: Any

class FilterRefBase(Mapping):
    filter_id: Any
    filter_options: Any
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __len__(self): ...
    def __iter__(self): ...
    def __getitem__(self, item): ...

class Gzip(FilterRefBase):
    filter_id: Any
    filter_options: Any
    def __init__(self, level=...) -> None: ...

def fill_dcpl(
    plist,
    shape,
    dtype,
    chunks,
    compression,
    compression_opts,
    shuffle,
    fletcher32,
    maxshape,
    scaleoffset,
    external,
    allow_unknown_filter: bool = ...,
): ...
def get_filters(plist): ...

CHUNK_BASE: Any
CHUNK_MIN: Any
CHUNK_MAX: Any

def guess_chunk(shape, maxshape, typesize): ...
