import scala.util.{Try, Using}
import scala.io.Source

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
    return Source.fromFile(fileName).getLines.toList
  }

  def calcFuel(moduleMass:Int, acc:Int) : Int = {
    if (moduleMass == 0)
      return acc
    val fuelRequired = (moduleMass/3).toInt - 2
    if (fuelRequired <= 0)
      return acc
    else
      return calcFuel(fuelRequired, acc + fuelRequired)
  }

}


