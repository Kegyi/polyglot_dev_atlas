from abc import ABC, abstractmethod
from typing import Optional

class Request:
    def __init__(self, level: int, message: str):
        self.level = level
        self.message = message

class Handler(ABC):
    def __init__(self):
        self.next: Optional[Handler] = None
    
    def set_next(self, handler: "Handler") -> "Handler":
        self.next = handler
        return handler
    
    @abstractmethod
    def handle(self, request: Request) -> str:
        pass

class LowHandler(Handler):
    def handle(self, request: Request) -> str:
        if request.level <= 1:
            return f"LowHandler: {request.message}"
        return self.next.handle(request) if self.next else ""

class MidHandler(Handler):
    def handle(self, request: Request) -> str:
        if request.level == 2:
            return f"MidHandler: {request.message}"
        return self.next.handle(request) if self.next else ""

class HighHandler(Handler):
    def handle(self, request: Request) -> str:
        if request.level >= 3:
            return f"HighHandler: {request.message}"
        return ""

low = LowHandler()
mid = MidHandler()
high = HighHandler()

low.set_next(mid).set_next(high)

print(low.handle(Request(1, "Simple")))
print(low.handle(Request(2, "Normal")))
print(low.handle(Request(3, "Critical")))
