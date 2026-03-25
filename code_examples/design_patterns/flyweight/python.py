class GlyphStyle:
    def __init__(self, font: str) -> None:
        self.font = font


class StyleFactory:
    def __init__(self) -> None:
        self._styles: dict[str, GlyphStyle] = {}

    def get(self, font: str) -> GlyphStyle:
        if font not in self._styles:
            self._styles[font] = GlyphStyle(font)
        return self._styles[font]


factory = StyleFactory()
first = factory.get("mono-12")
second = factory.get("mono-12")
print(first is second)
