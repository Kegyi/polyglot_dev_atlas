// Abstract Factory
trait UIElement

case class Button(label: String) extends UIElement
case class Checkbox(label: String) extends UIElement

trait UIFactory {
  def createButton(label: String): Button
  def createCheckbox(label: String): Checkbox
}

object LightThemeFactory extends UIFactory {
  def createButton(label: String): Button = Button(s"Light Button: $label")
  def createCheckbox(label: String): Checkbox = Checkbox(s"Light Checkbox: $label")
}

object DarkThemeFactory extends UIFactory {
  def createButton(label: String): Button = Button(s"Dark Button: $label")
  def createCheckbox(label: String): Checkbox = Checkbox(s"Dark Checkbox: $label")
}

object Main extends App {
  val lightFactory: UIFactory = LightThemeFactory
  val darkFactory: UIFactory = DarkThemeFactory
  
  println(lightFactory.createButton("OK"))
  println(darkFactory.createButton("OK"))
}
