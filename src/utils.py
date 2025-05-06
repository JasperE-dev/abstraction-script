from dataclasses import dataclass as struct
from enum import Enum as enum
from enum import auto

class tokenKind(enum):
    unknown=auto()
    word=auto()
    number=auto()
    operator=auto()
    syntax=auto()
    newLine=auto()
    string     =auto()
    keyword    =auto()
    #statement   =auto()
    #expression =auto()
    block      =auto()
    none=auto()

    def __repr__(self)->str:
        return f'{self}'[10:]

@struct
class Location:
    line:int
    column:int
    def __str__(self):
        return f"{self.line}:{self.column}"

@struct
class token:
    kind:tokenKind
    symbol:str
    location:Location

    def __repr__(self)->str:
        return f'token<{self.kind.__str__()[10:]}, {self.symbol.__repr__()}, {self.location.line}:{self.location.column}>'

@struct
class toke:
    kind:tokenKind
    lexeme:str
    location:Location