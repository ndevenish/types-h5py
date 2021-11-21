from typing import Any, ClassVar

import h5py._objects
import h5py.h5py_warnings

CYTHON_VERSION_COMPILED_WITH: str
HDF5_VERSION_COMPILED_AGAINST: tuple
INDEX_CRT_ORDER: int
INDEX_NAME: int
ITER_DEC: int
ITER_INC: int
ITER_NATIVE: int
NUMPY_VERSION_COMPILED_AGAINST: str

def get_libversion(*args, **kwargs) -> Any: ...

phil: h5py._objects.FastRLock

class ByteStringContext:
    def __init__(self) -> None: ...
    def __bool__(self) -> Any: ...
    def __enter__(self) -> Any: ...
    def __exit__(self, *args) -> Any: ...
    def __nonzero__(self) -> Any: ...

class H5PYConfig:
    API_16: Any
    API_18: Any
    _bytestrings: Any
    _default_file_mode: Any
    _f_name: Any
    _i_name: Any
    _r_name: Any
    _t_name: Any
    _track_order: Any
    bool_names: Any
    complex_names: Any
    default_file_mode: Any
    mpi: Any
    read_byte_strings: Any
    ros3: Any
    swmr_min_hdf5_version: Any
    track_order: Any
    vds_min_hdf5_version: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class H5pyDeprecationWarning(h5py.h5py_warnings.H5pyWarning): ...

def get_config(*args, **kwargs) -> Any: ...
