// Factory Method
trait Vehicle {
    def drive(): String
}

case class Car() extends Vehicle {
    def drive(): String = "Driving a car on road"
}

case class Truck() extends Vehicle {
    def drive(): String = "Driving a truck on highway"
}

trait Factory {
    def createVehicle(): Vehicle
}

object CarFactory extends Factory {
    def createVehicle(): Vehicle = Car()
}

object TruckFactory extends Factory {
    def createVehicle(): Vehicle = Truck()
}

object Main extends App {
    val carFactory: Factory = CarFactory
    val truckFactory: Factory = TruckFactory
    
    println(carFactory.createVehicle().drive())
    println(truckFactory.createVehicle().drive())
}
