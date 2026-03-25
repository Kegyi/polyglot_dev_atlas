# Modern Python Command using plain callables
# No Command ABC or class hierarchy - commands are just Callable[[], None].
from typing import Callable

class Device:
    def turn_on(self) -> None:
        print("Device is ON")

    def turn_off(self) -> None:
        print("Device is OFF")

device = Device()

# Commands are plain callables - bound methods, lambdas, or closures
commands: list[Callable[[], None]] = [
    device.turn_on,
    device.turn_off,
]

for cmd in commands:
    cmd()
