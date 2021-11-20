from typing import Any

import h5py._objects

DISABLE_EDC: int
ENABLE_EDC: int
ERROR_EDC: int
FILTER_ALL: int
FILTER_CONFIG_DECODE_ENABLED: int
FILTER_CONFIG_ENCODE_ENABLED: int
FILTER_DEFLATE: int
FILTER_ERROR: int
FILTER_FLETCHER32: int
FILTER_LZF: int
FILTER_MAX: int
FILTER_NBIT: int
FILTER_NONE: int
FILTER_RESERVED: int
FILTER_SCALEOFFSET: int
FILTER_SHUFFLE: int
FILTER_SZIP: int
FLAG_DEFMASK: int
FLAG_INVMASK: int
FLAG_MANDATORY: int
FLAG_OPTIONAL: int
FLAG_REVERSE: int
FLAG_SKIP_EDC: int
NO_EDC: int
SO_FLOAT_DSCALE: int
SO_FLOAT_ESCALE: int
SO_INT: int
SO_INT_MINBITS_DEFAULT: int
SZIP_ALLOW_K13_OPTION_MASK: int
SZIP_CHIP_OPTION_MASK: int
SZIP_EC_OPTION_MASK: int
SZIP_MAX_PIXELS_PER_BLOCK: int
SZIP_NN_OPTION_MASK: int

def filter_avail(*args, **kwargs) -> Any: ...
def get_filter_info(*args, **kwargs) -> Any: ...

phil: h5py._objects.FastRLock

def unregister_filter(*args, **kwargs) -> Any: ...
def _register_lzf(*args, **kwargs) -> Any: ...
def with_phil(*args, **kwargs) -> Any: ...
