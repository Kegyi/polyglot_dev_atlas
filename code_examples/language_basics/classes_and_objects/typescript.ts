#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

class Person {
  constructor(public name: string, public age: number) {}

  describe(): string {
    return `${this.name} is ${this.age} years old`;
  }

  birthday(): void {
    this.age += 1;
  }
}

function main(): void {
  const person = new Person("Alice", 29);
  console.log(person.describe());
  person.birthday();
  console.log(person.describe());
}

main();
setImmediate(() => {});
