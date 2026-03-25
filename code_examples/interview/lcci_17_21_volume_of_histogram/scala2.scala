object Solution {
  def trap(height: Array[Int]): Int = {
    var left = 0; var right = height.length - 1
    var leftMax = 0; var rightMax = 0; var ans = 0
    while (left < right) {
      if (height(left) < height(right)) {
        if (height(left) >= leftMax) leftMax = height(left)
        else ans += leftMax - height(left)
        left += 1
      } else {
        if (height(right) >= rightMax) rightMax = height(right)
        else ans += rightMax - height(right)
        right -= 1
      }
    }
    ans
  }
}
