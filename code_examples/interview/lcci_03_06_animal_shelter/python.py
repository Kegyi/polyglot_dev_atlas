from collections import deque


class AnimalShelter:
    def __init__(self) -> None:
        self.ticket = 0
        self.dogs: deque[tuple[int, int]] = deque()
        self.cats: deque[tuple[int, int]] = deque()

    def enqueue(self, animal_id: int, animal_type: str) -> None:
        item = (self.ticket, animal_id)
        self.ticket += 1
        if animal_type == "dog":
            self.dogs.append(item)
        else:
            self.cats.append(item)

    def dequeue_any(self) -> int:
        if not self.dogs and not self.cats:
            return -1
        if not self.dogs:
            return self.dequeue_cat()
        if not self.cats:
            return self.dequeue_dog()
        if self.dogs[0][0] < self.cats[0][0]:
            return self.dequeue_dog()
        return self.dequeue_cat()

    def dequeue_dog(self) -> int:
        return self.dogs.popleft()[1] if self.dogs else -1

    def dequeue_cat(self) -> int:
        return self.cats.popleft()[1] if self.cats else -1


def main() -> None:
    shelter = AnimalShelter()
    shelter.enqueue(1, "dog")
    shelter.enqueue(2, "cat")
    shelter.enqueue(3, "dog")
    print(shelter.dequeue_any())
    print(shelter.dequeue_cat())
    print(shelter.dequeue_dog())
    print(shelter.dequeue_any())


if __name__ == "__main__":
    main()
