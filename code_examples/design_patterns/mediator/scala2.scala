// Mediator
trait ChatMediator {
    def sendMessage(sender: ChatUser, msg: String): Unit
}

class ChatRoom extends ChatMediator {
    private var user1: Option[ChatUser] = None
    private var user2: Option[ChatUser] = None
    
    def addUsers(u1: ChatUser, u2: ChatUser): Unit = {
        user1 = Some(u1)
        user2 = Some(u2)
    }
    
    def sendMessage(sender: ChatUser, msg: String): Unit = {
        if (sender == user1.orNull) {
            user2.foreach(_.receive(msg))
        } else {
            user1.foreach(_.receive(msg))
        }
    }
}

class ChatUser(name: String, mediator: ChatMediator) {
    def send(msg: String): Unit = {
        println(s"$name sends: $msg")
        mediator.sendMessage(this, msg)
    }
    
    def receive(msg: String): Unit = {
        println(s"$name receives: $msg")
    }
}

object Main extends App {
    val room = new ChatRoom()
    val u1 = new ChatUser("Alice", room)
    val u2 = new ChatUser("Bob", room)
    
    room.addUsers(u1, u2)
    
    u1.send("Hello!")
    u2.send("Hi there!")
}
