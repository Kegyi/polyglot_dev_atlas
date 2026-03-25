# Modern Python Observer using function callbacks
# No Observer ABC or subclasses - any callable with the right signature subscribes directly.
from typing import Callable

class Subject:
    def __init__(self) -> None:
        self._listeners: list[Callable[[str], None]] = []

    def subscribe(self, listener: Callable[[str], None]) -> None:
        self._listeners.append(listener)

    def notify(self, msg: str) -> None:
        for listener in self._listeners:
            listener(msg)

subject = Subject()

# Lambdas or regular functions - no Observer subclass needed
subject.subscribe(lambda msg: print(f"Observer1 received: {msg}"))
subject.subscribe(lambda msg: print(f"Observer2 received: {msg}"))

subject.notify("Event 1")
subject.notify("Event 2")
