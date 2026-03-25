type Animal = {
  order: number;
  id: number;
};

class AnimalShelter {
  private ticket = 0;
  private dogs: Animal[] = [];
  private cats: Animal[] = [];

  enqueue(id: number, kind: "dog" | "cat"): void {
    const item: Animal = { order: this.ticket, id };
    this.ticket += 1;
    if (kind === "dog") {
      this.dogs.push(item);
    } else {
      this.cats.push(item);
    }
  }

  dequeueAny(): number {
    if (!this.dogs.length && !this.cats.length) {
      return -1;
    }
    if (!this.dogs.length) {
      return this.dequeueCat();
    }
    if (!this.cats.length) {
      return this.dequeueDog();
    }
    return this.dogs[0].order < this.cats[0].order ? this.dequeueDog() : this.dequeueCat();
  }

  dequeueDog(): number {
    return this.dogs.length ? this.dogs.shift()!.id : -1;
  }

  dequeueCat(): number {
    return this.cats.length ? this.cats.shift()!.id : -1;
  }
}

function main(): void {
  const shelter = new AnimalShelter();
  shelter.enqueue(1, "dog");
  shelter.enqueue(2, "cat");
  shelter.enqueue(3, "dog");
  console.log(shelter.dequeueAny());
  console.log(shelter.dequeueCat());
  console.log(shelter.dequeueDog());
  console.log(shelter.dequeueAny());
}

main();
