object Lcci0208LinkedListCycle:
  final case class ListNode(var value: Int, var next: ListNode | Null = null)

  def buildList(nums: Vector[Int]): ListNode | Null =
    val dummy = ListNode(0, null)
    var tail: ListNode = dummy
    nums.foreach { n =>
      tail.next = ListNode(n, null)
      tail = tail.next.asInstanceOf[ListNode]
    }
    dummy.next

  def hasCycle(head: ListNode | Null): Boolean =
    var slow = head
    var fast = head
    while (fast != null && fast.asInstanceOf[ListNode].next != null) {
      slow = slow.asInstanceOf[ListNode].next
      fast = fast.asInstanceOf[ListNode].next.asInstanceOf[ListNode].next
      if (slow == fast) return true
    }
    false

  @main def main(): Unit =
    val a = buildList(Vector(1, 2, 3, 4))
    var tail = a
    while (tail != null && tail.asInstanceOf[ListNode].next != null) {
      tail = tail.asInstanceOf[ListNode].next
    }
    if (tail != null && a != null && a.asInstanceOf[ListNode].next != null) {
      tail.asInstanceOf[ListNode].next = a.asInstanceOf[ListNode].next
    }

    val b = buildList(Vector(1, 2, 3, 4))

    println(hasCycle(a))
    println(hasCycle(b))
