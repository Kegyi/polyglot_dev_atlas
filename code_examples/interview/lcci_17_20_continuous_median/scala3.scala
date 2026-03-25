import scala.collection.mutable

class MedianFinder:
  // lo: max-heap, hi: min-heap
  private val lo = mutable.PriorityQueue[Int]()        // max-heap
  private val hi = mutable.PriorityQueue[Int]()(Ordering[Int].reverse) // min-heap

  def addNum(num: Int): Unit =
    lo.enqueue(num)
    hi.enqueue(lo.dequeue())
    if (hi.size > lo.size) lo.enqueue(hi.dequeue())

  def findMedian(): Double =
    if (lo.size > hi.size) lo.head.toDouble
    else (lo.head + hi.head) / 2.0
