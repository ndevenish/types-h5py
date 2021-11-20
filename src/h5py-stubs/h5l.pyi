from typing import Any, ClassVar

import h5py._objects

TYPE_EXTERNAL: int
TYPE_HARD: int
TYPE_SOFT: int
phil: h5py._objects.FastRLock

class LinkInfo:
    corder: Any
    corder_valid: Any
    cset: Any
    type: Any
    u: Any
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class LinkProxy:
    def __init__(self, *args, **kwargs) -> None: ...
    def create_external(self, *args, **kwargs) -> Any: ...
    def create_hard(self, *args, **kwargs) -> Any: ...
    def create_soft(self, *args, **kwargs) -> Any: ...
    def exists(self, *args, **kwargs) -> Any: ...
    def get_info(self, *args, **kwargs) -> Any: ...
    def get_val(self, *args, **kwargs) -> Any: ...
    def iterate(self, *args, **kwargs) -> Any: ...
    def move(self, *args, **kwargs) -> Any: ...
    def visit(self, *args, **kwargs) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __hash__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class _LinkVisitor:
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

def with_phil(*args, **kwargs) -> Any: ...
