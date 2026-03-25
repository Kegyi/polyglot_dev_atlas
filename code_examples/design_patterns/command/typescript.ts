interface ICommand {
    execute(): void;
}

class Receiver {
    turnOn(): void {
        console.log("Device is ON");
    }
    
    turnOff(): void {
        console.log("Device is OFF");
    }
}

class TurnOnCommand implements ICommand {
    constructor(private receiver: Receiver) {}
    
    execute(): void {
        this.receiver.turnOn();
    }
}

class TurnOffCommand implements ICommand {
    constructor(private receiver: Receiver) {}
    
    execute(): void {
        this.receiver.turnOff();
    }
}

class Invoker {
    private commands: ICommand[] = [];
    
    addCommand(command: ICommand): void {
        this.commands.push(command);
    }
    
    executeAll(): void {
        for (const cmd of this.commands) {
            cmd.execute();
        }
    }
}

const device = new Receiver();
const invoker = new Invoker();

invoker.addCommand(new TurnOnCommand(device));
invoker.addCommand(new TurnOffCommand(device));

invoker.executeAll();
