// Memento
case class Memento(state: String)

class Originator(private var state: String):
    def setState(s: String): Unit =
        state = s
    
    def getState: String = state
    
    def saveState(): Memento = Memento(state)
    
    def restoreState(memento: Memento): Unit =
        state = memento.state

class Caretaker:
    private var history: List[Memento] = List()
    
    def save(memento: Memento): Unit =
        history = history :+ memento
    
    def restore(index: Int): Option[Memento] =
        if (index >= 0 && index < history.length) Some(history(index))
        else None

@main def main(): Unit =
    val originator = new Originator("State 1")
    val caretaker = new Caretaker()
    
    caretaker.save(originator.saveState())
    
    originator.setState("State 2")
    caretaker.save(originator.saveState())
    
    originator.setState("State 3")
    println(s"Current: ${originator.getState}")
    
    caretaker.restore(0).foreach(originator.restoreState)
    println(s"Restored: ${originator.getState}")
