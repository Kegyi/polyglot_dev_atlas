// Command
class Device {
    def turnOn(): Unit = println("Device is ON")
    def turnOff(): Unit = println("Device is OFF")
}

trait Command {
    def execute(): Unit
}

class TurnOnCommand(device: Device) extends Command {
    def execute(): Unit = device.turnOn()
}

class TurnOffCommand(device: Device) extends Command {
    def execute(): Unit = device.turnOff()
}

class Invoker {
    private var commands: List[Command] = List()
    
    def addCommand(cmd: Command): Unit = {
        commands = commands :+ cmd
    }
    
    def executeAll(): Unit = {
        commands.foreach(_.execute())
    }
}

object Main extends App {
    val device = new Device()
    val invoker = new Invoker()
    
    invoker.addCommand(new TurnOnCommand(device))
    invoker.addCommand(new TurnOffCommand(device))
    
    invoker.executeAll()
}
