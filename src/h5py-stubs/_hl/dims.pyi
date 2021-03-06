from .. import h5ds
from ..h5py_warnings import H5pyDeprecationWarning
from . import base
from .base import phil, with_phil
from .dataset import Dataset

class DimensionProxy(base.CommonStateObject):
    @property
    def label(self): ...
    @label.setter
    def label(self, val) -> None: ...
    def __init__(self, id_, dimension) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __iter__(self): ...
    def __len__(self): ...
    def __getitem__(self, item): ...
    def attach_scale(self, dset) -> None: ...
    def detach_scale(self, dset) -> None: ...
    def items(self): ...
    def keys(self): ...
    def values(self): ...

class DimensionManager(base.CommonStateObject):
    def __init__(self, parent) -> None: ...
    def __getitem__(self, index): ...
    def __len__(self): ...
    def __iter__(self): ...
    def create_scale(self, dset, name: str = ...) -> None: ...
