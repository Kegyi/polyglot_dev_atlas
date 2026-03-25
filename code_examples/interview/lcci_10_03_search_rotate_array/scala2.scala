object Lcci1003SearchRotateArray {
    def search(arr: Array[Int], target: Int): Int = {
        if (arr.isEmpty) {
            return -1
        }
        var left = 0
        var right = arr.length - 1
        while (left < right && arr(left) == arr(right)) {
            right -= 1
        }
        while (left < right) {
            val mid = (left + right) / 2
            if (arr(mid) > arr(right)) {
                if (arr(left) <= target && target <= arr(mid)) right = mid else left = mid + 1
            } else if (arr(mid) < arr(right)) {
                if (arr(mid) < target && target <= arr(right)) left = mid + 1 else right = mid
            } else {
                right -= 1
            }
        }
        if (arr(left) == target) left else -1
    }

    def main(args: Array[String]): Unit = {
        val arr = Array(15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14)
        println(search(arr, 5))
        println(search(arr, 11))
    }
}
