# Modern Python Chain of Responsibility using a flat list of callables
# No linked-list of handler subclasses - handlers are plain functions returning bool.
from typing import Callable
from dataclasses import dataclass

@dataclass
class Request:
    level: int
    message: str

Handler = Callable[[Request], bool]

def process(chain: list[Handler], req: Request) -> None:
    for handler in chain:
        if handler(req):
            return

def low_handler(req: Request) -> bool:
    if req.level > 1:
        return False
    print(f"LowLevelHandler: {req.message}")
    return True

def mid_handler(req: Request) -> bool:
    if req.level != 2:
        return False
    print(f"MidLevelHandler: {req.message}")
    return True

def high_handler(req: Request) -> bool:
    print(f"HighLevelHandler: {req.message}")
    return True

chain: list[Handler] = [low_handler, mid_handler, high_handler]

process(chain, Request(1, "low request"))
process(chain, Request(2, "mid request"))
process(chain, Request(3, "high request"))
