from dataclasses import dataclass

@dataclass
class Color:
    red: int = 255
    green: int = 255
    blue: int = 255

@dataclass
class Lightning:
    strip: any
    color: Color