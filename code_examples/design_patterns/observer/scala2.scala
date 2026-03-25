// Observer
trait Observer {
    def update(msg: String): Unit
}

class Subject {
    private var observers: List[Observer] = List()
    
    def attach(observer: Observer): Unit = {
        observers = observers :+ observer
    }
    
    def notify(msg: String): Unit = {
        observers.foreach(_.update(msg))
    }
}

class ConcreteObserver(name: String) extends Observer {
    def update(msg: String): Unit = {
        println(s"$name received: $msg")
    }
}

object Main extends App {
    val subject = new Subject()
    val obs1 = new ConcreteObserver("Observer1")
    val obs2 = new ConcreteObserver("Observer2")
    
    subject.attach(obs1)
    subject.attach(obs2)
    
    subject.notify("Event 1")
    subject.notify("Event 2")
}
