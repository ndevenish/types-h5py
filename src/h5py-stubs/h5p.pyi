from typing import Any

import h5py._objects

CRT_ORDER_INDEXED: int
CRT_ORDER_TRACKED: int
DATASET_ACCESS: PropClassID
DATASET_CREATE: PropClassID
DATASET_XFER: PropClassID
DEFAULT: None
FILE_ACCESS: PropClassID
FILE_CREATE: PropClassID
GROUP_CREATE: PropClassID
LINK_ACCESS: PropClassID
LINK_CREATE: PropClassID
NO_CLASS: PropClassID
OBJECT_COPY: PropClassID
OBJECT_CREATE: PropClassID

def create(*args, **kwargs) -> Any: ...

phil: h5py._objects.FastRLock

class PropClassID(PropID):
    def __init__(self, *args, **kwargs) -> None: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __hash__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class PropCopyID(PropInstanceID):
    def __init__(self, *args, **kwargs) -> None: ...
    def get_copy_object(self, *args, **kwargs) -> Any: ...
    def set_copy_object(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class PropCreateID(PropInstanceID):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class PropDAID(PropInstanceID):
    def __init__(self, *args, **kwargs) -> None: ...
    def get_chunk_cache(self, *args, **kwargs) -> Any: ...
    def get_virtual_prefix(self, *args, **kwargs) -> Any: ...
    def get_virtual_printf_gap(self, *args, **kwargs) -> Any: ...
    def get_virtual_view(self, *args, **kwargs) -> Any: ...
    def set_chunk_cache(self, *args, **kwargs) -> Any: ...
    def set_virtual_prefix(self, *args, **kwargs) -> Any: ...
    def set_virtual_printf_gap(self, *args, **kwargs) -> Any: ...
    def set_virtual_view(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class PropDCID(PropOCID):
    def __init__(self, *args, **kwargs) -> None: ...
    def _has_filter(self, *args, **kwargs) -> Any: ...
    def all_filters_avail(self, *args, **kwargs) -> Any: ...
    def fill_value_defined(self, *args, **kwargs) -> Any: ...
    def get_alloc_time(self, *args, **kwargs) -> Any: ...
    def get_chunk(self, *args, **kwargs) -> Any: ...
    def get_external(self, *args, **kwargs) -> Any: ...
    def get_external_count(self, *args, **kwargs) -> Any: ...
    def get_fill_time(self, *args, **kwargs) -> Any: ...
    def get_fill_value(self, *args, **kwargs) -> Any: ...
    def get_filter(self, *args, **kwargs) -> Any: ...
    def get_filter_by_id(self, *args, **kwargs) -> Any: ...
    def get_layout(self, *args, **kwargs) -> Any: ...
    def get_nfilters(self, *args, **kwargs) -> Any: ...
    def get_virtual_count(self, *args, **kwargs) -> Any: ...
    def get_virtual_dsetname(self, *args, **kwargs) -> Any: ...
    def get_virtual_filename(self, *args, **kwargs) -> Any: ...
    def get_virtual_srcspace(self, *args, **kwargs) -> Any: ...
    def get_virtual_vspace(self, *args, **kwargs) -> Any: ...
    def remove_filter(self, *args, **kwargs) -> Any: ...
    def set_alloc_time(self, *args, **kwargs) -> Any: ...
    def set_chunk(self, *args, **kwargs) -> Any: ...
    def set_deflate(self, *args, **kwargs) -> Any: ...
    def set_external(self, *args, **kwargs) -> Any: ...
    def set_fill_time(self, *args, **kwargs) -> Any: ...
    def set_fill_value(self, *args, **kwargs) -> Any: ...
    def set_filter(self, *args, **kwargs) -> Any: ...
    def set_fletcher32(self, *args, **kwargs) -> Any: ...
    def set_layout(self, *args, **kwargs) -> Any: ...
    def set_scaleoffset(self, *args, **kwargs) -> Any: ...
    def set_shuffle(self, *args, **kwargs) -> Any: ...
    def set_szip(self, *args, **kwargs) -> Any: ...
    def set_virtual(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class PropDXID(PropInstanceID):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class PropFAID(PropInstanceID):
    def __init__(self, *args, **kwargs) -> None: ...
    def get_alignment(self, *args, **kwargs) -> Any: ...
    def get_cache(self, *args, **kwargs) -> Any: ...
    def get_driver(self, *args, **kwargs) -> Any: ...
    def get_fapl_core(self, *args, **kwargs) -> Any: ...
    def get_fapl_family(self, *args, **kwargs) -> Any: ...
    def get_fapl_ros3(self, *args, **kwargs) -> Any: ...
    def get_fclose_degree(self, *args, **kwargs) -> Any: ...
    def get_libver_bounds(self, *args, **kwargs) -> Any: ...
    def get_mdc_config(self, *args, **kwargs) -> Any: ...
    def get_sieve_buf_size(self, *args, **kwargs) -> Any: ...
    def set_alignment(self, *args, **kwargs) -> Any: ...
    def set_cache(self, *args, **kwargs) -> Any: ...
    def set_driver(self, *args, **kwargs) -> Any: ...
    def set_fapl_core(self, *args, **kwargs) -> Any: ...
    def set_fapl_family(self, *args, **kwargs) -> Any: ...
    def set_fapl_log(self, *args, **kwargs) -> Any: ...
    def set_fapl_ros3(self, *args, **kwargs) -> Any: ...
    def set_fapl_sec2(self, *args, **kwargs) -> Any: ...
    def set_fapl_split(self, *args, **kwargs) -> Any: ...
    def set_fapl_stdio(self, *args, **kwargs) -> Any: ...
    def set_fclose_degree(self, *args, **kwargs) -> Any: ...
    def set_file_image(self, *args, **kwargs) -> Any: ...
    def set_fileobj_driver(self, *args, **kwargs) -> Any: ...
    def set_libver_bounds(self, *args, **kwargs) -> Any: ...
    def set_mdc_config(self, *args, **kwargs) -> Any: ...
    def set_sieve_buf_size(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class PropFCID(PropOCID):
    def __init__(self, *args, **kwargs) -> None: ...
    def get_file_space_strategy(self, *args, **kwargs) -> Any: ...
    def get_link_creation_order(self, *args, **kwargs) -> Any: ...
    def get_sizes(self, *args, **kwargs) -> Any: ...
    def get_userblock(self, *args, **kwargs) -> Any: ...
    def get_version(self, *args, **kwargs) -> Any: ...
    def set_file_space_strategy(self, *args, **kwargs) -> Any: ...
    def set_link_creation_order(self, *args, **kwargs) -> Any: ...
    def set_sizes(self, *args, **kwargs) -> Any: ...
    def set_userblock(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class PropGCID(PropOCID):
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def get_link_creation_order(self, *args, **kwargs) -> Any: ...
    def set_link_creation_order(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class PropID(h5py._objects.ObjectID):
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def equal(self, *args, **kwargs) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __hash__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class PropInstanceID(PropID):
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def copy(self, *args, **kwargs) -> Any: ...
    def get_class(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class PropLAID(PropInstanceID):
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def get_elink_fapl(self, *args, **kwargs) -> Any: ...
    def get_elink_prefix(self, *args, **kwargs) -> Any: ...
    def get_nlinks(self, *args, **kwargs) -> Any: ...
    def set_elink_fapl(self, *args, **kwargs) -> Any: ...
    def set_elink_prefix(self, *args, **kwargs) -> Any: ...
    def set_nlinks(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class PropLCID(PropCreateID):
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def get_char_encoding(self, *args, **kwargs) -> Any: ...
    def get_create_intermediate_group(self, *args, **kwargs) -> Any: ...
    def set_char_encoding(self, *args, **kwargs) -> Any: ...
    def set_create_intermediate_group(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class PropOCID(PropCreateID):
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def get_attr_creation_order(self, *args, **kwargs) -> Any: ...
    def get_attr_phase_change(self, *args, **kwargs) -> Any: ...
    def get_obj_track_times(self, *args, **kwargs) -> Any: ...
    def set_attr_creation_order(self, *args, **kwargs) -> Any: ...
    def set_attr_phase_change(self, *args, **kwargs) -> Any: ...
    def set_obj_track_times(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class PropTCID(PropOCID):
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

def with_phil(*args, **kwargs) -> Any: ...
