from abc import ABC, abstractmethod

class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: "User", event: str) -> None:
        pass

class User:
    def __init__(self, mediator: Mediator, name: str):
        self.mediator = mediator
        self.name = name
    
    def send(self, msg: str) -> None:
        print(f"{self.name} sends: {msg}")
        self.mediator.notify(self, msg)
    
    def receive(self, msg: str) -> None:
        print(f"{self.name} receives: {msg}")

class ChatRoom(Mediator):
    def __init__(self):
        self.user1: User = None
        self.user2: User = None
    
    def add_users(self, u1: User, u2: User) -> None:
        self.user1 = u1
        self.user2 = u2
    
    def notify(self, sender: User, event: str) -> None:
        if sender == self.user1:
            self.user2.receive(event)
        else:
            self.user1.receive(event)

room = ChatRoom()
u1 = User(room, "Alice")
u2 = User(room, "Bob")

room.add_users(u1, u2)

u1.send("Hello!")
u2.send("Hi there!")
