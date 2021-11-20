from typing import Any, ClassVar

import h5py._objects

CRT_ORDER_TRACKED: int
DATASET: int
GROUP: int
LINK: int
LINK_ERROR: int
LINK_HARD: int
LINK_SOFT: int
TYPE: int
UNKNOWN: int

def _path_valid(*args, **kwargs) -> Any: ...
def create(*args, **kwargs) -> Any: ...
def get_objinfo(*args, **kwargs) -> Any: ...
def iterate(*args, **kwargs) -> Any: ...
def open(*args, **kwargs) -> Any: ...

phil: h5py._objects.FastRLock

class GroupID(h5py._objects.ObjectID):
    links: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def get_comment(self, *args, **kwargs) -> Any: ...
    def get_create_plist(self, *args, **kwargs) -> Any: ...
    def get_linkval(self, *args, **kwargs) -> Any: ...
    def get_num_objs(self, *args, **kwargs) -> Any: ...
    def get_objname_by_idx(self, *args, **kwargs) -> Any: ...
    def get_objtype_by_idx(self, *args, **kwargs) -> Any: ...
    def link(self, *args, **kwargs) -> Any: ...
    def move(self, *args, **kwargs) -> Any: ...
    def set_comment(self, *args, **kwargs) -> Any: ...
    def unlink(self, *args, **kwargs) -> Any: ...
    def __contains__(self, other) -> Any: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class GroupIter:
    def __init__(self, *args, **kwargs) -> None: ...
    def __iter__(self) -> Any: ...
    def __next__(self) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class GroupStat:
    fileno: Any
    linklen: Any
    mtime: Any
    nlink: Any
    objno: Any
    type: Any
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def _hash(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class _GroupVisitor:
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

def with_phil(*args, **kwargs) -> Any: ...