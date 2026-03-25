object Lcci0306AnimalShelter {
  final case class Animal(order: Int, id: Int)

  final class AnimalShelter {
    private var ticket = 0
    private val dogs = scala.collection.mutable.Queue.empty[Animal]
    private val cats = scala.collection.mutable.Queue.empty[Animal]

    def enqueue(id: Int, kind: String): Unit = {
      val item = Animal(ticket, id)
      ticket += 1
      if (kind == "dog") dogs.enqueue(item) else cats.enqueue(item)
    }

    def dequeueAny(): Int = {
      if (dogs.isEmpty && cats.isEmpty) return -1
      if (dogs.isEmpty) return dequeueCat()
      if (cats.isEmpty) return dequeueDog()
      if (dogs.front.order < cats.front.order) dequeueDog() else dequeueCat()
    }

    def dequeueDog(): Int = if (dogs.isEmpty) -1 else dogs.dequeue().id

    def dequeueCat(): Int = if (cats.isEmpty) -1 else cats.dequeue().id
  }

  def main(args: Array[String]): Unit = {
    val shelter = new AnimalShelter
    shelter.enqueue(1, "dog")
    shelter.enqueue(2, "cat")
    shelter.enqueue(3, "dog")
    println(shelter.dequeueAny())
    println(shelter.dequeueCat())
    println(shelter.dequeueDog())
    println(shelter.dequeueAny())
  }
}
