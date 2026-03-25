from abc import ABC, abstractmethod

class Receiver:
    def turn_on(self):
        print("Device is ON")
    
    def turn_off(self):
        print("Device is OFF")

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

class TurnOnCommand(Command):
    def __init__(self, receiver: Receiver):
        self.receiver = receiver
    
    def execute(self) -> None:
        self.receiver.turn_on()

class TurnOffCommand(Command):
    def __init__(self, receiver: Receiver):
        self.receiver = receiver
    
    def execute(self) -> None:
        self.receiver.turn_off()

class Invoker:
    def __init__(self):
        self.commands: list[Command] = []
    
    def add_command(self, command: Command) -> None:
        self.commands.append(command)
    
    def execute_all(self) -> None:
        for cmd in self.commands:
            cmd.execute()

device = Receiver()
invoker = Invoker()

invoker.add_command(TurnOnCommand(device))
invoker.add_command(TurnOffCommand(device))

invoker.execute_all()
