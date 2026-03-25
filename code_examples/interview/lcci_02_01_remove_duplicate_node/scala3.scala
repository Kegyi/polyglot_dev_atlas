object Lcci0201RemoveDuplicateNode:
  final case class ListNode(var value: Int, var next: ListNode | Null = null)

  def buildList(nums: Vector[Int]): ListNode | Null =
    val dummy = ListNode(0, null)
    var tail: ListNode = dummy
    nums.foreach { n =>
      tail.next = ListNode(n, null)
      tail = tail.next.asInstanceOf[ListNode]
    }
    dummy.next

  def removeDuplicateNodes(head: ListNode | Null): Unit =
    val seen = scala.collection.mutable.HashSet.empty[Int]
    var prev: ListNode | Null = null
    var cur = head

    while (cur != null) {
      val node = cur.asInstanceOf[ListNode]
      if (seen.contains(node.value)) {
        prev.asInstanceOf[ListNode].next = node.next
        cur = node.next
      } else {
        seen += node.value
        prev = cur
        cur = node.next
      }
    }

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
    val head = buildList(Vector(1, 2, 3, 3, 2, 1, 4))
    removeDuplicateNodes(head)
    printList(head)
