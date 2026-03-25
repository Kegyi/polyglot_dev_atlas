// Decorator
trait Notification {
    def send(): Unit
}

class BasicNotification extends Notification {
    def send(): Unit = print("Sending notification")
}

class EmailNotification(notif: Notification) extends Notification {
    def send(): Unit = {
        notif.send()
        print(" + Email")
    }
}

class SMSNotification(notif: Notification) extends Notification {
    def send(): Unit = {
        notif.send()
        print(" + SMS")
    }
}

object Main extends App {
    var notif: Notification = new BasicNotification()
    notif = new EmailNotification(notif)
    notif = new SMSNotification(notif)
    
    notif.send()
    println()
}
