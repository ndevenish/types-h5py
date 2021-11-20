import logging
from typing import Any

import h5py.h5

cfg: h5py.h5.H5PYConfig
getLogger: function
logger: logging.Logger

def get_config(*args, **kwargs) -> Any: ...
def register_converters(*args, **kwargs) -> Any: ...
def unregister_converters(*args, **kwargs) -> Any: ...
