object Lcci0205SumLists:
  final case class ListNode(var value: Int, var next: ListNode | Null = null)

  def buildList(nums: Vector[Int]): ListNode | Null =
    val dummy = ListNode(0, null)
    var tail: ListNode = dummy
    nums.foreach { n =>
      tail.next = ListNode(n, null)
      tail = tail.next.asInstanceOf[ListNode]
    }
    dummy.next

  def addTwoNumbers(a: ListNode | Null, b: ListNode | Null): ListNode | Null =
    val dummy = ListNode(0, null)
    var tail: ListNode = dummy
    var l1 = a
    var l2 = b
    var carry = 0

    while (l1 != null || l2 != null || carry > 0) {
      var sum = carry
      if (l1 != null) {
        sum += l1.asInstanceOf[ListNode].value
        l1 = l1.asInstanceOf[ListNode].next
      }
      if (l2 != null) {
        sum += l2.asInstanceOf[ListNode].value
        l2 = l2.asInstanceOf[ListNode].next
      }
      tail.next = ListNode(sum % 10, null)
      tail = tail.next.asInstanceOf[ListNode]
      carry = sum / 10
    }

    dummy.next

  def printList(head: ListNode | Null): Unit =
    val out = scala.collection.mutable.ArrayBuffer.empty[Int]
    var cur = head
    while (cur != null) {
      out += cur.asInstanceOf[ListNode].value
      cur = cur.asInstanceOf[ListNode].next
    }
    println(out.mkString(" "))

  @main def main(): Unit =
    val a = buildList(Vector(7, 1, 6))
    val b = buildList(Vector(5, 9, 2))
    printList(addTwoNumbers(a, b))
