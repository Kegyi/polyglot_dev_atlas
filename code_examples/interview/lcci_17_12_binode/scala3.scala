class TreeNode(var value: Int, var left: TreeNode = null, var right: TreeNode = null)

object Lcci1712BiNode:
  private var prev: TreeNode = _

  private def inorder(root: TreeNode): Unit = {
    if (root == null) return
    inorder(root.left)
    root.left = null
    prev.right = root
    prev = root
    inorder(root.right)
  }

  def convertBiNode(root: TreeNode): TreeNode =
    val dummy = new TreeNode(0)
    prev = dummy
    inorder(root)
    dummy.right

  @main def main(): Unit =
    val root = new TreeNode(4)
    root.left = new TreeNode(2)
    root.right = new TreeNode(5)
    root.left.left = new TreeNode(1)
    root.left.right = new TreeNode(3)
    root.right.right = new TreeNode(6)
    root.left.left.left = new TreeNode(0)

    var head = convertBiNode(root)
    val out = scala.collection.mutable.ArrayBuffer[Int]()
    while (head != null) {
      out += head.value
      head = head.right
    }
    println(out.mkString(" ")) // 0 1 2 3 4 5 6
