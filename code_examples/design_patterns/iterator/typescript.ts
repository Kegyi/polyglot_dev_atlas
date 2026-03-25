interface IIterator {
    hasNext(): boolean;
    next(): number;
}

interface ICollection {
    createIterator(): IIterator;
}

class ArrayIterator implements IIterator {
    private position = 0;
    
    constructor(private items: number[]) {}
    
    hasNext(): boolean {
        return this.position < this.items.length;
    }
    
    next(): number {
        return this.items[this.position++];
    }
}

class ArrayCollection implements ICollection {
    private items: number[] = [];
    
    add(item: number): void {
        this.items.push(item);
    }
    
    createIterator(): IIterator {
        return new ArrayIterator(this.items);
    }
}

const collection = new ArrayCollection();
collection.add(10);
collection.add(20);
collection.add(30);

const it = collection.createIterator();
let result = "";
while (it.hasNext()) {
    result += it.next() + " ";
}
console.log(result);
