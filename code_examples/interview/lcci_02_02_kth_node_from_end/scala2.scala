object Lcci0202KthNodeFromEnd {
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

  def kthToLast(head: ListNode, k: Int): Int = {
    var fast: ListNode | Null = head
    var slow: ListNode | Null = head

    for (_ <- 0 until k) {
      fast = fast.asInstanceOf[ListNode].next
    }

    while (fast != null) {
      fast = fast.asInstanceOf[ListNode].next
      slow = slow.asInstanceOf[ListNode].next
    }

    slow.asInstanceOf[ListNode].value
  }

  def main(args: Array[String]): Unit = {
    val head = buildList(Vector(1, 2, 3, 4, 5)).asInstanceOf[ListNode]
    println(kthToLast(head, 2))
  }
}
