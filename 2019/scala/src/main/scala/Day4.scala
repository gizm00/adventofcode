

object Day4 extends App {
  val MIN = 34
  val MAX = 56

  def hasSameAdjacent(i: Int): Boolean = {
    val vecOfI = i.toString.map(_.asDigit)
    // is there a way to map over vecOfI and compare i, i+1?
    val adjacents = vecOfI.sliding(2).toList
      .filter(n => n(0) == n(1))
      .map(_(0))

    adjacents.length > 0
  }

  def isNotDecreasing(i: Int): Boolean = {
    val vecOfI = i.toString.map(_.asDigit)
    val checkSameOrIncreasing = vecOfI.sliding(2)
      .filter(n => n(0) <= n(1))
      .map(_(0)).toList

    // hm, checkSameOrIncreasing will be missing the last digit, so
    // how to compare to vecOfI?
  }

  def getPasswords(minimum: Int, maximum: Int) : List[Int] = {
    val range = List.range(minimum, maximum)
    range
      .filter(hasSameAdjacent(_))
      .filter(isNotDecreasing(_))
  }

  print(s"Found ${getPasswords(MIN, MAX).length} passwords")

}
