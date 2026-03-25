class Person(var name: String, var age: Int) {
  def describe(): String = s"$name is $age years old"

  def birthday(): Unit = {
    age += 1
  }
}

object ClassesAndObjectsBasics {
  def main(args: Array[String]): Unit = {
    val person = new Person("Alice", 29)
    println(person.describe())
    person.birthday()
    println(person.describe())
  }
}
