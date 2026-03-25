# Modern Python State using structural pattern matching (Python 3.10+)
# No State ABC or subclass hierarchy - states are plain dataclasses.
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class StartState:
    pass

@dataclass
class RunningState:
    pass

@dataclass
class StoppedState:
    pass

type State = StartState | RunningState | StoppedState  # Python 3.12+

def handle(state: StartState | RunningState | StoppedState) -> None:
    match state:
        case StartState():
            print("Entering start state")
        case RunningState():
            print("Running state active")
        case StoppedState():
            print("Stopped state active")

state: StartState | RunningState | StoppedState = StartState()
handle(state)

state = RunningState()
handle(state)

state = StoppedState()
handle(state)
