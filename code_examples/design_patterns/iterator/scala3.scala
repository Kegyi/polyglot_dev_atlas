// Iterator
trait CustomIterator[T]:
    def hasNext: Boolean
    def next(): T

trait CustomCollection[T]:
    def createIterator(): CustomIterator[T]

class ArrayIterator[T](items: Vector[T]) extends CustomIterator[T]:
    private var position = 0
    
    def hasNext: Boolean = position < items.length
    
    def next(): T =
        val result = items(position)
        position += 1
        result

class ArrayCollection[T](items: Vector[T]) extends CustomCollection[T]:
    def createIterator(): CustomIterator[T] = new ArrayIterator(items)

@main def main(): Unit =
    val collection = new ArrayCollection(Vector(10, 20, 30))
    val it = collection.createIterator()
    
    while (it.hasNext) {
        print(it.next() + " ")
    }
    println()
