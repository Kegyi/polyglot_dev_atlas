// Chain of Responsibility
case class Request(level: Int, message: String)

trait Handler:
    protected var next: Option[Handler] = None
    
    def setNext(h: Handler): Handler =
        next = Some(h)
        h
    
    def handle(req: Request): Unit

class LowHandler extends Handler:
    def handle(req: Request): Unit =
        if (req.level <= 1) {
            println(s"LowHandler: ${req.message}")
        } else {
            next.foreach(_.handle(req))
        }

class MidHandler extends Handler:
    def handle(req: Request): Unit =
        if (req.level == 2) {
            println(s"MidHandler: ${req.message}")
        } else {
            next.foreach(_.handle(req))
        }

class HighHandler extends Handler:
    def handle(req: Request): Unit =
        if (req.level >= 3) {
            println(s"HighHandler: ${req.message}")
        }

@main def main(): Unit =
    val low = new LowHandler()
    val mid = new MidHandler()
    val high = new HighHandler()
    
    low.setNext(mid).setNext(high)
    
    low.handle(Request(1, "Simple"))
    low.handle(Request(2, "Normal"))
    low.handle(Request(3, "Critical"))
