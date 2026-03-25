// Flyweight
case class GlyphStyle(font: String, size: Int)

class Glyph(char: Char, style: GlyphStyle):
    def render(): Unit = println(s"$char in ${style.font}")

class GlyphFactory:
    private var cache: Map[GlyphStyle, GlyphStyle] = Map()
    
    def getStyle(font: String, size: Int): GlyphStyle =
        val key = GlyphStyle(font, size)
        cache.getOrElse(key, {
            cache = cache + (key -> key)
            key
        })

@main def main(): Unit =
    val factory = new GlyphFactory()
    
    val style1 = factory.getStyle("Arial", 12)
    val style2 = factory.getStyle("Arial", 12)
    
    val glyph1 = new Glyph('A', style1)
    val glyph2 = new Glyph('B', style2)
    
    glyph1.render()
    glyph2.render()
