from dataclasses import dataclass
from copy import deepcopy


@dataclass
class Report:
    title: str
    tags: list[str]

    def clone(self) -> "Report":
        return deepcopy(self)


template = Report("weekly", ["ops", "summary"])
copy = template.clone()

print(template)
print(copy)