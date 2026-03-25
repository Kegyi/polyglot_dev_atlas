#!/usr/bin/env python3
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int

    def describe(self) -> str:
        return f"{self.name} is {self.age} years old"

    def birthday(self) -> None:
        self.age += 1


def main() -> None:
    person = Person("Alice", 29)
    print(person.describe())
    person.birthday()
    print(person.describe())


if __name__ == "__main__":
    main()
