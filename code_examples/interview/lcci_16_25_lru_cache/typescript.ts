class DLinkedNode {
    key: number;
    val: number;
    prev: DLinkedNode | null = null;
    next: DLinkedNode | null = null;

    constructor(key: number, val: number) {
        this.key = key;
        this.val = val;
    }
}

class LRUCache {
    private readonly capacity: number;
    private readonly map = new Map<number, DLinkedNode>();
    private readonly head = new DLinkedNode(0, 0);
    private readonly tail = new DLinkedNode(0, 0);

    constructor(capacity: number) {
        this.capacity = capacity;
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }

    private remove(node: DLinkedNode): void {
        node.prev!.next = node.next;
        node.next!.prev = node.prev;
    }

    private addFront(node: DLinkedNode): void {
        node.next = this.head.next;
        node.prev = this.head;
        this.head.next!.prev = node;
        this.head.next = node;
    }

    get(key: number): number {
        const node = this.map.get(key);
        if (!node) return -1;
        this.remove(node);
        this.addFront(node);
        return node.val;
    }

    put(key: number, value: number): void {
        const node = this.map.get(key);
        if (node) {
            node.val = value;
            this.remove(node);
            this.addFront(node);
            return;
        }
        if (this.map.size === this.capacity) {
            const lru = this.tail.prev!;
            this.remove(lru);
            this.map.delete(lru.key);
        }
        const fresh = new DLinkedNode(key, value);
        this.addFront(fresh);
        this.map.set(key, fresh);
    }
}

const cache = new LRUCache(2);
cache.put(1, 1);
cache.put(2, 2);
console.log(cache.get(1));
cache.put(3, 3);
console.log(cache.get(2));
cache.put(4, 4);
console.log(cache.get(1));
console.log(cache.get(3));
console.log(cache.get(4));
