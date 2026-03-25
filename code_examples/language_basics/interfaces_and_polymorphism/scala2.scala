trait Speaker {
  def speak(): String
}

class Dog extends Speaker {
  override def speak(): String = "woof"
}

class Cat extends Speaker {
  override def speak(): String = "meow"
}

object InterfacesAndPolymorphismBasics {
  def main(args: Array[String]): Unit = {
    val speakers: Seq[Speaker] = Seq(new Dog, new Cat)
    speakers.foreach(speaker => println(speaker.speak()))
  }
}
