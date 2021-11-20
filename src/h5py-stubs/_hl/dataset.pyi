from typing import Any

from .. import h5, h5d, h5ds, h5fd, h5p, h5r, h5s, h5t
from . import filters
from .base import Empty, HLObject, find_item_type, phil, with_phil
from .compat import filename_decode
from .datatype import Datatype
from .vds import VDSmap, vds_support

MPI: Any

def make_new_dset(
    parent,
    shape: Any | None = ...,
    dtype: Any | None = ...,
    data: Any | None = ...,
    name: Any | None = ...,
    chunks: Any | None = ...,
    compression: Any | None = ...,
    shuffle: Any | None = ...,
    fletcher32: Any | None = ...,
    maxshape: Any | None = ...,
    compression_opts: Any | None = ...,
    fillvalue: Any | None = ...,
    scaleoffset: Any | None = ...,
    track_times: Any | None = ...,
    external: Any | None = ...,
    track_order: Any | None = ...,
    dcpl: Any | None = ...,
    allow_unknown_filter: bool = ...,
): ...

class AstypeWrapper:
    def __init__(self, dset, dtype) -> None: ...
    def __getitem__(self, args): ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...

class AsStrWrapper:
    dset: Any
    encoding: Any
    errors: Any
    def __init__(self, dset, encoding, errors: str = ...) -> None: ...
    def __getitem__(self, args): ...

class FieldsWrapper:
    extract_field: Any
    dset: Any
    read_dtype: Any
    def __init__(self, dset, prior_dtype, names) -> None: ...
    def __getitem__(self, args): ...

def readtime_dtype(basetype, names): ...

class CollectiveContext:
    def __init__(self, dset) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args) -> None: ...

class ChunkIterator:
    def __init__(self, dset, source_sel: Any | None = ...) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...

class Dataset(HLObject):
    def astype(self, dtype): ...
    def asstr(self, encoding: Any | None = ..., errors: str = ...): ...
    def fields(self, names, *, _prior_dtype: Any | None = ...): ...
    @property
    def collective(self): ...
    @property
    def dims(self): ...
    @property
    def ndim(self): ...
    @property
    def shape(self): ...
    @shape.setter
    def shape(self, shape) -> None: ...
    @property
    def size(self): ...
    @property
    def nbytes(self): ...
    @property
    def dtype(self): ...
    @property
    def chunks(self): ...
    @property
    def compression(self): ...
    @property
    def compression_opts(self): ...
    @property
    def shuffle(self): ...
    @property
    def fletcher32(self): ...
    @property
    def scaleoffset(self): ...
    @property
    def external(self): ...
    @property
    def maxshape(self): ...
    @property
    def fillvalue(self): ...
    def __init__(self, bind, *, readonly: bool = ...) -> None: ...
    def resize(self, size, axis: Any | None = ...) -> None: ...
    def __len__(self): ...
    def len(self): ...
    def __iter__(self): ...
    def iter_chunks(self, sel: Any | None = ...): ...
    def __getitem__(self, args, new_dtype: Any | None = ...): ...
    def __setitem__(self, args, val) -> None: ...
    def read_direct(
        self, dest, source_sel: Any | None = ..., dest_sel: Any | None = ...
    ) -> None: ...
    def write_direct(
        self, source, source_sel: Any | None = ..., dest_sel: Any | None = ...
    ) -> None: ...
    def __array__(self, dtype: Any | None = ...): ...
    def refresh(self) -> None: ...
    def flush(self) -> None: ...
    @property
    def is_virtual(self): ...
    def virtual_sources(self): ...
    def make_scale(self, name: str = ...) -> None: ...