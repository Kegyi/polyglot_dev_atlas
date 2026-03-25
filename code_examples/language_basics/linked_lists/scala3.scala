object LinkedListBasics:
  case class Node(value: Int, next: Option[Node] = None)

  def printList(head: Option[Node]): Unit =
    val parts = Iterator.unfold(head) {
      case None       => None
      case Some(node) => Some((node.value.toString, node.next))
    }
    println(parts.mkString(" -> "))

  def prepend(head: Option[Node], value: Int): Node = Node(value, head)

  def removeValue(head: Option[Node], value: Int): Option[Node] = head match {
    case None                              => None
    case Some(node) if node.value == value => node.next
    case Some(node)                        => Some(node.copy(next = removeValue(node.next, value)))
  }

  @main def main(): Unit =
    var head: Option[Node] = None
    for (v <- List(3, 2, 1)) head = Some(prepend(head, v))  // 1 -> 2 -> 3
    printList(head)
    head = removeValue(head, 2)
    printList(head)  // 1 -> 3
