from typing import Any

from .. import h5r, h5s
from .base import product

def select(shape, args, dataset: Any | None = ...): ...

class Selection:
    def __init__(self, shape, spaceid: Any | None = ...) -> None: ...
    @property
    def id(self): ...
    @property
    def shape(self): ...
    @property
    def nselect(self): ...
    @property
    def mshape(self): ...
    @property
    def array_shape(self): ...
    def expand_shape(self, source_shape): ...
    def broadcast(self, source_shape) -> None: ...
    def __getitem__(self, args) -> None: ...

class PointSelection(Selection):
    def __init__(
        self, shape, spaceid: Any | None = ..., points: Any | None = ...
    ) -> None: ...
    @classmethod
    def from_mask(cls, mask, spaceid: Any | None = ...): ...
    def append(self, points) -> None: ...
    def prepend(self, points) -> None: ...
    def set(self, points) -> None: ...

class SimpleSelection(Selection):
    @property
    def mshape(self): ...
    @property
    def array_shape(self): ...
    def __init__(
        self, shape, spaceid: Any | None = ..., hyperslab: Any | None = ...
    ) -> None: ...
    def expand_shape(self, source_shape): ...
    def broadcast(self, source_shape) -> None: ...

class FancySelection(Selection):
    @property
    def mshape(self): ...
    @property
    def array_shape(self): ...
    def __init__(
        self,
        shape,
        spaceid: Any | None = ...,
        mshape: Any | None = ...,
        array_shape: Any | None = ...,
    ) -> None: ...
    def expand_shape(self, source_shape): ...
    def broadcast(self, source_shape) -> None: ...

def guess_shape(sid): ...