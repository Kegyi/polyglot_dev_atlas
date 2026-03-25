object Lcci0206PalindromeLinkedList {
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

  def reverseList(head: ListNode | Null): ListNode | Null = {
    var prev: ListNode | Null = null
    var cur = head
    while (cur != null) {
      val node = cur.asInstanceOf[ListNode]
      val nextNode = node.next
      node.next = prev
      prev = node
      cur = nextNode
    }
    prev
  }

  def isPalindrome(head: ListNode | Null): Boolean = {
    if (head == null || head.asInstanceOf[ListNode].next == null) return true

    var slow = head
    var fast = head
    while (fast != null && fast.asInstanceOf[ListNode].next != null) {
      slow = slow.asInstanceOf[ListNode].next
      fast = fast.asInstanceOf[ListNode].next.asInstanceOf[ListNode].next
    }

    var p1 = head
    var p2 = reverseList(slow)
    while (p2 != null) {
      if (p1.asInstanceOf[ListNode].value != p2.asInstanceOf[ListNode].value) return false
      p1 = p1.asInstanceOf[ListNode].next
      p2 = p2.asInstanceOf[ListNode].next
    }
    true
  }

  def main(args: Array[String]): Unit = {
    val a = buildList(Vector(1, 2, 2, 1))
    val b = buildList(Vector(1, 2, 3, 2, 1))
    println(isPalindrome(a))
    println(isPalindrome(b))
  }
}
