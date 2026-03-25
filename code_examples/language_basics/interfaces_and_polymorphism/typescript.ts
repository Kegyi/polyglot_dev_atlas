#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

interface Speaker {
  speak(): string;
}

class Dog implements Speaker {
  speak(): string {
    return "woof";
  }
}

class Cat implements Speaker {
  speak(): string {
    return "meow";
  }
}

function main(): void {
  const speakers: Speaker[] = [new Dog(), new Cat()];
  for (const speaker of speakers) {
    console.log(speaker.speak());
  }
}

main();
setImmediate(() => {});
