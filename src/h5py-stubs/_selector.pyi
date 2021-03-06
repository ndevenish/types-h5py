from typing import Any, Optional

class MultiBlockSlice:
    def __init__(
        self,
        start: int = ...,
        stride: int = ...,
        count: Optional[int] = ...,
        block: int = ...,
    ) -> None: ...
    def _repr(self, count: Optional[int] = ...) -> Any: ...
    def indices(self, length: int) -> Any: ...

class Reader:
    def __init__(self, *args, **kwargs) -> None: ...
    def read(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class Selector:
    def __init__(self, *args, **kwargs) -> None: ...
    def make_selection(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...
