// Modern TypeScript Observer using typed function callbacks
// No Observer interface or class hierarchy - listeners are plain typed callbacks.

type Listener<T> = (event: T) => void;

class Subject<T> {
    private listeners: Array<Listener<T>> = [];

    subscribe(listener: Listener<T>): void {
        this.listeners.push(listener);
    }

    notify(event: T): void {
        this.listeners.forEach(l => l(event));
    }
}

const subject = new Subject<string>();

subject.subscribe(msg => console.log(`Observer1 received: ${msg}`));
subject.subscribe(msg => console.log(`Observer2 received: ${msg}`));

subject.notify("Event 1");
subject.notify("Event 2");
