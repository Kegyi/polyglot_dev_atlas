// Modern Scala State using sealed trait ADT + pattern matching (Scala 3)
// No State trait or subclass hierarchy - states are plain ADT cases.
// Transitions are just variable reassignments.

sealed trait State
case object StartState   extends State
case object RunningState extends State
case object StoppedState extends State

def handle(state: State): Unit = state match
  case StartState   => println("Entering start state")
  case RunningState => println("Running state active")
  case StoppedState => println("Stopped state active")

@main def stateModernExample(): Unit =
  var state: State = StartState
  handle(state)

  state = RunningState
  handle(state)

  state = StoppedState
  handle(state)
