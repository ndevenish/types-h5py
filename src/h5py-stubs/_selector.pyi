from typing import Any, ClassVar

class MultiBlockSlice:
    def __init__(self, *args, **kwargs) -> None: ...
    def _repr(self, *args, **kwargs) -> Any: ...
    def indices(self, *args, **kwargs) -> Any: ...

class Reader:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def read(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class Selector:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def make_selection(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...
