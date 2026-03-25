# Modern Python Visitor using functools.singledispatch
# No accept/visit ceremony - shapes are plain dataclasses, operations are functions.
from __future__ import annotations
from dataclasses import dataclass
from functools import singledispatch

@dataclass
class Circle:
    pass

@dataclass
class Rectangle:
    pass

# --- Operation 1: draw ---
@singledispatch
def draw(shape: object) -> None:
    raise NotImplementedError(f"draw not implemented for {type(shape)}")

@draw.register
def _(shape: Circle) -> None:
    print("Drawing circle")

@draw.register
def _(shape: Rectangle) -> None:
    print("Drawing rectangle")

# --- Operation 2: describe - added without touching shape types ---
@singledispatch
def describe(shape: object) -> str:
    raise NotImplementedError(f"describe not implemented for {type(shape)}")

@describe.register
def _(shape: Circle) -> str:
    return "it's a circle"

@describe.register
def _(shape: Rectangle) -> str:
    return "it's a rectangle"

draw(Circle())
draw(Rectangle())
print(describe(Circle()))
print(describe(Rectangle()))
