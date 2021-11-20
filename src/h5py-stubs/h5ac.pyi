from typing import Any, ClassVar

class CacheConfig:
    apply_empty_reserve: Any
    apply_max_decrement: Any
    apply_max_increment: Any
    decr_mode: Any
    decrement: Any
    dirty_bytes_threshold: Any
    empty_reserve: Any
    epoch_length: Any
    epochs_before_eviction: Any
    evictions_enabled: Any
    flash_incr_mode: Any
    flash_multiple: Any
    flash_threshold: Any
    incr_mode: Any
    increment: Any
    initial_size: Any
    lower_hr_threshold: Any
    max_decrement: Any
    max_increment: Any
    max_size: Any
    min_clean_fraction: Any
    min_size: Any
    rpt_fcn_enabled: Any
    set_initial_size: Any
    upper_hr_threshold: Any
    version: Any
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...
