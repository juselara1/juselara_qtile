from pydantic import BaseModel, PositiveInt
from typing import List, Optional

class Defaults(BaseModel):
    n_screens: PositiveInt
    wallpaper: str
    wallpaper_mode: str
    time_format: str

class KeySwitch(BaseModel):
    left: List[str]
    right: List[str]
    up: List[str]
    down: List[str]
    next: List[str]

class KeyMove(BaseModel):
    shuffle_left: List[str]
    shuffle_right: List[str]
    shuffle_up: List[str]
    shuffle_down: List[str]

class KeyResize(BaseModel):
    grow_left: List[str]
    grow_right: List[str]
    grow_up: List[str]
    grow_down: List[str]

class KeyUtils(BaseModel):
    normalize: List[str]
    maximize: List[str]
    next_screen: List[str]
    quit: List[str]

class KeyCustom(BaseModel):
    kitty: List[str]
    rofi: List[str]

class KeyStop(BaseModel):
    restart: List[str]
    shutdown: List[str]

class KeyGroups(BaseModel):
    key1: Optional[List[str]]
    key2: Optional[List[str]]
    key3: Optional[List[str]]
    key4: Optional[List[str]]
    key5: Optional[List[str]]
    key6: Optional[List[str]]
    key7: Optional[List[str]]
    key8: Optional[List[str]]
    key9: Optional[List[str]]
    key0: Optional[List[str]]

class Keys(BaseModel):
    switch: KeySwitch
    move: KeyMove
    resize: KeyResize
    utils: KeyUtils
    custom: KeyCustom
    stop: KeyStop
    keygroups: KeyGroups

class Font(BaseModel):
    font: str
    fontsize: PositiveInt

class Spacing(BaseModel):
    margin: PositiveInt
    border_width: PositiveInt
    padding: PositiveInt

class Colors(BaseModel):
    color0: str
    color1: str
    color2: str
    color3: str
    color4: str

class PathsConfig(BaseModel):
    defaults: Defaults
    keys: Keys
    font: Font
    spacing: Spacing
    colors: Colors
