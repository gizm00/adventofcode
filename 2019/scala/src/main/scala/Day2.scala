import scala.collection.mutable.ArrayBuffer


object Day2 extends App{

  var day2_input = ArrayBuffer[Int](1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,5,23,1,23,9,27,2,27,6,31,1,31,6,35,2,35,9,39,1,6,39,43,2,10,43,47,1,47,9,51,1,51,6,55,1,55,6,59,2,59,10,63,1,6,63,67,2,6,67,71,1,71,5,75,2,13,75,79,1,10,79,83,1,5,83,87,2,87,10,91,1,5,91,95,2,95,6,99,1,99,6,103,2,103,6,107,2,107,9,111,1,111,5,115,1,115,6,119,2,6,119,123,1,5,123,127,1,127,13,131,1,2,131,135,1,135,10,0,99,2,14,0,0)

  def executeIntcodeProgram(memory: ArrayBuffer[Int]) = {
    var memPtr = 0
    while (memory(memPtr) != 99 && memPtr < memory.length) {
      memPtr = executeIntcodeCommand(memory, memPtr)

      // memPtr will be at the end of the last instruction, increment
      memPtr += 1
    }
  }

  def restoreGravityAssist(memory: ArrayBuffer[Int]) = {
    memory(1) = 12
    memory(2) = 2
  }

  def executeIntcodeCommand(memory: ArrayBuffer[Int], memPtr: Int): Int = {
    memory(memPtr) match {
      case 1 => doOp1(memory, memPtr)
      case 2 => doOp2(memory, memPtr)
      case _ => memPtr
    }
  }



  def doOp1(memory: ArrayBuffer[Int], memPtr: Int): Int = {
    /*
    Add items at pointer +1 and pointer +2, putting result into
    pointer+3
    */
    memory(memory(memPtr+3)) = memory(memory(memPtr+2)) + memory(memory(memPtr+1))
    memPtr + 3
  }

  def doOp2(memory: ArrayBuffer[Int], memPtr: Int): Int = {
    /*
    Multiply items at pointer +1 and pointer +2, putting result into
    pointer+3
    */
    memory(memory(memPtr+3)) = memory(memory(memPtr+2)) * memory(memory(memPtr+1))
    memPtr + 3
  }

  restoreGravityAssist(day2_input)
  executeIntcodeProgram(day2_input)
  println(s"Value at memory location 0: ${day2_input(0)}")

}
