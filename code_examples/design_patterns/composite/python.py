from dataclasses import dataclass, field
from typing import Protocol


class Node(Protocol):
    def total_size(self) -> int: ...


@dataclass
class File:
    size: int

    def total_size(self) -> int:
        return self.size


@dataclass
class Folder:
    children: list[Node] = field(default_factory=list)

    def add(self, child: Node) -> None:
        self.children.append(child)

    def total_size(self) -> int:
        return sum(child.total_size() for child in self.children)


root = Folder()
root.add(File(5))
sub = Folder([File(7), File(3)])
root.add(sub)
print(root.total_size())
