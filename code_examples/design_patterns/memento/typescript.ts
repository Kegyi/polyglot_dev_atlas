class Memento {
    constructor(private state: string) {}
    
    getState(): string {
        return this.state;
    }
}

class Originator {
    private state: string = "";
    
    setState(state: string): void {
        this.state = state;
    }
    
    getState(): string {
        return this.state;
    }
    
    saveState(): Memento {
        return new Memento(this.state);
    }
    
    restoreState(memento: Memento): void {
        this.state = memento.getState();
    }
}

class Caretaker {
    private history: Memento[] = [];
    
    save(memento: Memento): void {
        this.history.push(memento);
    }
    
    restore(index: number): Memento | null {
        if (index >= 0 && index < this.history.length) {
            return this.history[index];
        }
        return null;
    }
}

const originator = new Originator();
const caretaker = new Caretaker();

originator.setState("State 1");
caretaker.save(originator.saveState());

originator.setState("State 2");
caretaker.save(originator.saveState());

originator.setState("State 3");
console.log(`Current: ${originator.getState()}`);

const restored = caretaker.restore(0);
if (restored) {
    originator.restoreState(restored);
    console.log(`Restored: ${originator.getState()}`);
}
