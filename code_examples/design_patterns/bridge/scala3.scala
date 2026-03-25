// Bridge
trait Sender:
    def send(msg: String): Unit

case class EmailSender() extends Sender:
    def send(msg: String): Unit = println(s"Email: $msg")

case class SMSSender() extends Sender:
    def send(msg: String): Unit = println(s"SMS: $msg")

abstract class Notification(sender: Sender) {
    def notify(msg: String): Unit = sender.send(msg)
}

class Alert(sender: Sender) extends Notification(sender)

@main def main(): Unit =
    val emailSender = EmailSender()
    val smsSender = SMSSender()
    
    val emailAlert = new Alert(emailSender)
    val smsAlert = new Alert(smsSender)
    
    emailAlert.notify("Test alert")
    smsAlert.notify("Test alert")
