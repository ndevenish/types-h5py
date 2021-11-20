from typing import Any, ClassVar

import h5py._objects

def create(*args, **kwargs) -> Any: ...
def delete(*args, **kwargs) -> Any: ...
def exists(*args, **kwargs) -> Any: ...
def get_info(*args, **kwargs) -> Any: ...
def get_num_attrs(*args, **kwargs) -> Any: ...
def iterate(*args, **kwargs) -> Any: ...
def open(*args, **kwargs) -> Any: ...

phil: h5py._objects.FastRLock

def rename(*args, **kwargs) -> Any: ...

class AttrID(h5py._objects.ObjectID):
    dtype: Any
    name: Any
    shape: Any
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def get_name(self, *args, **kwargs) -> Any: ...
    def get_space(self, *args, **kwargs) -> Any: ...
    def get_storage_size(self, *args, **kwargs) -> Any: ...
    def get_type(self, *args, **kwargs) -> Any: ...
    def read(self, *args, **kwargs) -> Any: ...
    def write(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class AttrInfo:
    corder: Any
    corder_valid: Any
    cset: Any
    data_size: Any
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def _hash(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class _AttrVisitor:
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

def with_phil(*args, **kwargs) -> Any: ...