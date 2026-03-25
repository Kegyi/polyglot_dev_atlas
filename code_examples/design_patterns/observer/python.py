from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, msg: str) -> None:
        pass

class Subject:
    def __init__(self):
        self.observers: list[Observer] = []
    
    def attach(self, observer: Observer) -> None:
        self.observers.append(observer)
    
    def notify(self, msg: str) -> None:
        for observer in self.observers:
            observer.update(msg)

class ConcreteObserver(Observer):
    def __init__(self, name: str):
        self.name = name
    
    def update(self, msg: str) -> None:
        print(f"{self.name} received: {msg}")

subject = Subject()
obs1 = ConcreteObserver("Observer1")
obs2 = ConcreteObserver("Observer2")

subject.attach(obs1)
subject.attach(obs2)

subject.notify("Event 1")
subject.notify("Event 2")
