class Memento:
    def __init__(self, state: str):
        self.state = state
    
    def get_state(self) -> str:
        return self.state

class Originator:
    def __init__(self):
        self.state = ""
    
    def set_state(self, state: str) -> None:
        self.state = state
    
    def get_state(self) -> str:
        return self.state
    
    def save_state(self) -> Memento:
        return Memento(self.state)
    
    def restore_state(self, memento: Memento) -> None:
        self.state = memento.get_state()

class Caretaker:
    def __init__(self):
        self.history: list[Memento] = []
    
    def save(self, memento: Memento) -> None:
        self.history.append(memento)
    
    def restore(self, index: int) -> Memento:
        if 0 <= index < len(self.history):
            return self.history[index]
        return None

originator = Originator()
caretaker = Caretaker()

originator.set_state("State 1")
caretaker.save(originator.save_state())

originator.set_state("State 2")
caretaker.save(originator.save_state())

originator.set_state("State 3")
print(f"Current: {originator.get_state()}")

originator.restore_state(caretaker.restore(0))
print(f"Restored: {originator.get_state()}")
