// Modern TypeScript State using discriminated union + exhaustive switch
// No IState interface or class hierarchy - states are plain tagged objects.

type StartState   = { kind: "start" };
type RunningState = { kind: "running" };
type StoppedState = { kind: "stopped" };

type State = StartState | RunningState | StoppedState;

function handle(state: State): void {
    switch (state.kind) {
        case "start":   console.log("Entering start state");  break;
        case "running": console.log("Running state active");   break;
        case "stopped": console.log("Stopped state active");   break;
        default: {
            const _exhaustive: never = state; // compile error on missing case
        }
    }
}

let state: State = { kind: "start" };
handle(state);

state = { kind: "running" };
handle(state);

state = { kind: "stopped" };
handle(state);
