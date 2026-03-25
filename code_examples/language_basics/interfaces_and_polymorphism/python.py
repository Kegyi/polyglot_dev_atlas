#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Speaker(ABC):
    @abstractmethod
    def speak(self) -> str:
        raise NotImplementedError


class Dog(Speaker):
    def speak(self) -> str:
        return "woof"


class Cat(Speaker):
    def speak(self) -> str:
        return "meow"


def main() -> None:
    speakers: list[Speaker] = [Dog(), Cat()]
    for speaker in speakers:
        print(speaker.speak())


if __name__ == "__main__":
    main()
