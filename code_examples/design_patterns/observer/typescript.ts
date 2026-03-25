interface IObserver {
    update(msg: string): void;
}

class Subject {
    private observers: IObserver[] = [];
    
    attach(observer: IObserver): void {
        this.observers.push(observer);
    }
    
    notify(msg: string): void {
        for (const observer of this.observers) {
            observer.update(msg);
        }
    }
}

class ConcreteObserver implements IObserver {
    constructor(private name: string) {}
    
    update(msg: string): void {
        console.log(`${this.name} received: ${msg}`);
    }
}

const subject = new Subject();
const obs1 = new ConcreteObserver("Observer1");
const obs2 = new ConcreteObserver("Observer2");

subject.attach(obs1);
subject.attach(obs2);

subject.notify("Event 1");
subject.notify("Event 2");
