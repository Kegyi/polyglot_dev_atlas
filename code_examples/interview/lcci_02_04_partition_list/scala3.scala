object Lcci0204PartitionList:
  final case class ListNode(var value: Int, var next: ListNode | Null = null)

  def buildList(nums: Vector[Int]): ListNode | Null =
    val dummy = ListNode(0, null)
    var tail: ListNode = dummy
    nums.foreach { n =>
      tail.next = ListNode(n, null)
      tail = tail.next.asInstanceOf[ListNode]
    }
    dummy.next

  def partition(head: ListNode | Null, x: Int): ListNode | Null =
    val lessDummy = ListNode(0, null)
    val greaterDummy = ListNode(0, null)
    var lessTail: ListNode = lessDummy
    var greaterTail: ListNode = greaterDummy
    var cur = head

    while (cur != null) {
      val node = cur.asInstanceOf[ListNode]
      if (node.value < x) {
        lessTail.next = node
        lessTail = node
      } else {
        greaterTail.next = node
        greaterTail = node
      }
      cur = node.next
    }

    greaterTail.next = null
    lessTail.next = greaterDummy.next
    lessDummy.next

  def printList(head: ListNode | Null): Unit =
    val out = scala.collection.mutable.ArrayBuffer.empty[Int]
    var cur = head
    while (cur != null) {
      val node = cur.asInstanceOf[ListNode]
      out += node.value
      cur = node.next
    }
    println(out.mkString(" "))

  @main def main(): Unit =
    val head = buildList(Vector(3, 5, 8, 5, 10, 2, 1))
    printList(partition(head, 5))
