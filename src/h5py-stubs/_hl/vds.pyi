from typing import Any

from .. import h5, h5d, h5p, h5s, h5t, version
from .compat import filename_encode
from .datatype import Datatype
from .selections import SimpleSelection, select

class VDSmap: ...

vds_support: bool
hdf5_version: Any

class VirtualSource:
    path: Any
    name: Any
    dtype: Any
    maxshape: Any
    sel: Any
    def __init__(
        self,
        path_or_dataset,
        name: Any | None = ...,
        shape: Any | None = ...,
        dtype: Any | None = ...,
        maxshape: Any | None = ...,
    ) -> None: ...
    @property
    def shape(self): ...
    def __getitem__(self, key): ...

class VirtualLayout:
    shape: Any
    dtype: Any
    maxshape: Any
    dcpl: Any
    def __init__(
        self, shape, dtype, maxshape: Any | None = ..., filename: Any | None = ...
    ) -> None: ...
    def __setitem__(self, key, source) -> None: ...
    def make_dataset(self, parent, name, fillvalue: Any | None = ...): ...
