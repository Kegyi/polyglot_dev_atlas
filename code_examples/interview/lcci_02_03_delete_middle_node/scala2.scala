object Lcci0203DeleteMiddleNode {
  final case class ListNode(var value: Int, var next: ListNode | Null = null)

  def buildList(nums: Vector[Int]): ListNode | Null = {
    val dummy = ListNode(0, null)
    var tail: ListNode = dummy
    nums.foreach { n =>
      tail.next = ListNode(n, null)
      tail = tail.next.asInstanceOf[ListNode]
    }
    dummy.next
  }

  def deleteMiddleNode(node: ListNode | Null): Boolean = {
    if (node == null || node.asInstanceOf[ListNode].next == null) {
      return false
    }
    val cur = node.asInstanceOf[ListNode]
    val next = cur.next.asInstanceOf[ListNode]
    cur.value = next.value
    cur.next = next.next
    true
  }

  def printList(head: ListNode | Null): Unit = {
    val out = scala.collection.mutable.ArrayBuffer.empty[Int]
    var cur = head
    while (cur != null) {
      val node = cur.asInstanceOf[ListNode]
      out += node.value
      cur = node.next
    }
    println(out.mkString(" "))
  }

  def main(args: Array[String]): Unit = {
    val head = buildList(Vector(1, 2, 3, 4, 5)).asInstanceOf[ListNode]
    deleteMiddleNode(head.next.asInstanceOf[ListNode].next)
    printList(head)
  }
}
