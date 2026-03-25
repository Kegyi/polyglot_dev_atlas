import java.security.MessageDigest
import java.util.zip.CRC32

object HashingAndChecksumsBasics:
  private def sha256Hex(text: String): String = {
    val digest = MessageDigest.getInstance("SHA-256").digest(text.getBytes("UTF-8"))
    digest.map(b => f"$b%02x").mkString
  }

  @main def main(): Unit =
    val text = "hello-world"
    val crc = new CRC32()
    crc.update(text.getBytes("UTF-8"))

    println(s"text: $text")
    println(s"sha256: ${sha256Hex(text)}")
    println(s"crc32: ${crc.getValue}")
