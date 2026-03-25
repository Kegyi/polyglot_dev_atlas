object Lcci0207IntersectionOfTwoLinkedLists:
  final case class ListNode(var value: Int, var next: ListNode | Null = null)

  def buildList(nums: Vector[Int]): ListNode | Null =
    val dummy = ListNode(0, null)
    var tail: ListNode = dummy
    nums.foreach { n =>
      tail.next = ListNode(n, null)
      tail = tail.next.asInstanceOf[ListNode]
    }
    dummy.next

  def getIntersectionNode(a: ListNode | Null, b: ListNode | Null): ListNode | Null =
    if (a == null || b == null) return null

    var p1 = a
    var p2 = b
    while (p1 != p2) {
      p1 = if (p1 != null) p1.asInstanceOf[ListNode].next else b
      p2 = if (p2 != null) p2.asInstanceOf[ListNode].next else a
    }
    p1

  @main def main(): Unit =
    val common = buildList(Vector(8, 10))
    val a = buildList(Vector(3, 1, 5, 9))
    val b = buildList(Vector(4, 6))

    var tailA = a
    while (tailA != null && tailA.asInstanceOf[ListNode].next != null) {
      tailA = tailA.asInstanceOf[ListNode].next
    }
    if (tailA != null) {
      tailA.asInstanceOf[ListNode].next = common
    }

    var tailB = b
    while (tailB != null && tailB.asInstanceOf[ListNode].next != null) {
      tailB = tailB.asInstanceOf[ListNode].next
    }
    if (tailB != null) {
      tailB.asInstanceOf[ListNode].next = common
    }

    val node = getIntersectionNode(a, b)
    println(if (node != null) node.asInstanceOf[ListNode].value else "null")
