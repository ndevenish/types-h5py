from typing import Any, ClassVar

import h5py._objects
import h5py.h5g

ACC_EXCL: int
ACC_RDONLY: int
ACC_RDWR: int
ACC_SWMR_READ: int
ACC_SWMR_WRITE: int
ACC_TRUNC: int
CLOSE_DEFAULT: int
CLOSE_SEMI: int
CLOSE_STRONG: int
CLOSE_WEAK: int
FILE_IMAGE_OPEN_RW: int
FSPACE_STRATEGY_AGGR: int
FSPACE_STRATEGY_FSM_AGGR: int
FSPACE_STRATEGY_NONE: int
FSPACE_STRATEGY_PAGE: int
LIBVER_EARLIEST: int
LIBVER_LATEST: int
LIBVER_V110: int
LIBVER_V18: int
OBJ_ALL: int
OBJ_ATTR: int
OBJ_DATASET: int
OBJ_DATATYPE: int
OBJ_FILE: int
OBJ_GROUP: int
OBJ_LOCAL: int
SCOPE_GLOBAL: int
SCOPE_LOCAL: int
UNLIMITED: int

def create(*args, **kwargs) -> Any: ...
def flush(*args, **kwargs) -> Any: ...
def get_name(*args, **kwargs) -> Any: ...
def get_obj_count(*args, **kwargs) -> Any: ...
def get_obj_ids(*args, **kwargs) -> Any: ...
def is_hdf5(*args, **kwargs) -> Any: ...
def mount(*args, **kwargs) -> Any: ...
def open(*args, **kwargs) -> Any: ...
def open_file_image(*args, **kwargs) -> Any: ...

phil: h5py._objects.FastRLock

def unmount(*args, **kwargs) -> Any: ...

class FileID(h5py.h5g.GroupID):
    name: Any
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def _close_open_objects(self, *args, **kwargs) -> Any: ...
    def close(self, *args, **kwargs) -> Any: ...
    def get_access_plist(self, *args, **kwargs) -> Any: ...
    def get_create_plist(self, *args, **kwargs) -> Any: ...
    def get_file_image(self, *args, **kwargs) -> Any: ...
    def get_filesize(self, *args, **kwargs) -> Any: ...
    def get_freespace(self, *args, **kwargs) -> Any: ...
    def get_intent(self, *args, **kwargs) -> Any: ...
    def get_mdc_config(self, *args, **kwargs) -> Any: ...
    def get_mdc_hit_rate(self, *args, **kwargs) -> Any: ...
    def get_mdc_size(self, *args, **kwargs) -> Any: ...
    def get_vfd_handle(self, *args, **kwargs) -> Any: ...
    def reopen(self, *args, **kwargs) -> Any: ...
    def reset_mdc_hit_rate_stats(self, *args, **kwargs) -> Any: ...
    def set_mdc_config(self, *args, **kwargs) -> Any: ...
    def start_swmr_write(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

def with_phil(*args, **kwargs) -> Any: ...
