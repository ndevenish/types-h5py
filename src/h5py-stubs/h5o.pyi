from typing import Any, ClassVar

import h5py._objects

COPY_EXPAND_EXT_LINK_FLAG: int
COPY_EXPAND_REFERENCE_FLAG: int
COPY_EXPAND_SOFT_LINK_FLAG: int
COPY_PRESERVE_NULL_FLAG: int
COPY_SHALLOW_HIERARCHY_FLAG: int
COPY_WITHOUT_ATTR_FLAG: int
TYPE_DATASET: int
TYPE_GROUP: int
TYPE_NAMED_DATATYPE: int

def copy(*args, **kwargs) -> Any: ...
def exists_by_name(*args, **kwargs) -> Any: ...
def get_comment(*args, **kwargs) -> Any: ...
def get_info(*args, **kwargs) -> Any: ...
def link(*args, **kwargs) -> Any: ...
def open(*args, **kwargs) -> Any: ...

phil: h5py._objects.FastRLock

def set_comment(*args, **kwargs) -> Any: ...
def visit(*args, **kwargs) -> Any: ...

class ObjInfo(_ObjInfo):
    hdr: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def __copy__(self) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class _OHdr(_ObjInfoBase):
    mesg: Any
    nmesgs: Any
    space: Any
    version: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def _hash(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class _OHdrMesg(_ObjInfoBase):
    present: Any
    shared: Any
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def _hash(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class _OHdrSpace(_ObjInfoBase):
    free: Any
    mesg: Any
    meta: Any
    total: Any
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def _hash(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class _ObjInfo(_ObjInfoBase):
    addr: Any
    fileno: Any
    rc: Any
    type: Any
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def _hash(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class _ObjInfoBase:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class _ObjectVisitor:
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

def with_phil(*args, **kwargs) -> Any: ...
