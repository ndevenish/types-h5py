from ..h5t import TypeID
from .base import HLObject, with_phil

class Datatype(HLObject):
    @property
    def dtype(self): ...
    def __init__(self, bind) -> None: ...
