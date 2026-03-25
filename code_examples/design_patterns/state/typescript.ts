interface IState {
    handle(): void;
}

class StartState implements IState {
    handle(): void {
        console.log("Entering start state");
    }
}

class RunningState implements IState {
    handle(): void {
        console.log("Running state active");
    }
}

class StoppedState implements IState {
    handle(): void {
        console.log("Stopped state active");
    }
}

class Context {
    private state: IState;
    
    setState(state: IState): void {
        this.state = state;
    }
    
    request(): void {
        this.state.handle();
    }
}

const ctx = new Context();

ctx.setState(new StartState());
ctx.request();

ctx.setState(new RunningState());
ctx.request();

ctx.setState(new StoppedState());
ctx.request();
