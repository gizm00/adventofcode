

object Day4 extends App {
  val MIN = 265275
  val MAX = 781584

  def hasSameAdjacent(digits: String): Boolean = {
    digits.zip(digits.tail).exists {
      case (i,j) => i == j
    }
  }

  def isDecreasing(digits: String): Boolean = {
    digits.zip(digits.tail).exists {
      case (i,j) => i > j
    }
  }

  def isManyEquals(digits: String): Boolean = {
    digits.zip(digits.tail).zip(digits.tail.tail).exists { case ((i, j), k) => (i == j && j == k) }
  }

  def getPasswords(minimum: Int, maximum: Int) : List[Int] = {
    val range = List.range(minimum, maximum)
    range
      .map(_.toString.map(_.asDigit))
      .filter(hasSameAdjacent)
      .filter(!isDecreasing)
      .filter(!isManyEquals)
  }

  print(s"Found ${getPasswords(MIN, MAX).length} passwords")

}