import scala.io.Source
import scala.annotation.tailrec

object Day1 extends App {
  def SOURCE_FILE = "/Users/gizmo/dev/adventofcode/2019/input_files/d1_input_module_masses.txt"

  val module_list = readFromFile(SOURCE_FILE)
  val fuelRequired = module_list
    .map(_.toInt)
    .map(calcFuel(_,0))
    .sum
  println(s"Required fuel: ${fuelRequired}")

  def readFromFile(fileName:String): List[String] = {
    // Figure out how to wrap in Using
    Source.fromFile(fileName).getLines.toList
  }

  @tailrec  // need this to tell scala that this is a tail recursive function
  def calcFuel(moduleMass:Int, acc:Int) : Int = {
    if (moduleMass == 0)
      acc
    val fuelRequired = (moduleMass/3).toInt - 2
    if (fuelRequired <= 0)
      acc
    else
      calcFuel(fuelRequired, acc + fuelRequired)
  }

  // Todo - property based testing

}


