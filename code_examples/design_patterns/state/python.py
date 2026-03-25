from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle(self) -> None:
        pass

class StartState(State):
    def handle(self) -> None:
        print("Entering start state")

class RunningState(State):
    def handle(self) -> None:
        print("Running state active")

class StoppedState(State):
    def handle(self) -> None:
        print("Stopped state active")

class Context:
    def __init__(self):
        self.state: State = None
    
    def set_state(self, state: State) -> None:
        self.state = state
    
    def request(self) -> None:
        self.state.handle()

ctx = Context()

ctx.set_state(StartState())
ctx.request()

ctx.set_state(RunningState())
ctx.request()

ctx.set_state(StoppedState())
ctx.request()
