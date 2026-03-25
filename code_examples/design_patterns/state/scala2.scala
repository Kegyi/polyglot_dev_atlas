// State
trait State {
    def handle(): Unit
}

class StartState extends State {
    def handle(): Unit = println("Entering start state")
}

class RunningState extends State {
    def handle(): Unit = println("Running state active")
}

class StoppedState extends State {
    def handle(): Unit = println("Stopped state active")
}

class Context(private var state: State) {
    def setState(s: State): Unit = {
        state = s
    }
    
    def request(): Unit = {
        state.handle()
    }
}

object Main extends App {
    val ctx = new Context(new StartState())
    
    ctx.request()
    
    ctx.setState(new RunningState())
    ctx.request()
    
    ctx.setState(new StoppedState())
    ctx.request()
}
