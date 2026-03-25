class GlyphStyle {
  constructor(public readonly font: string) {}
}

class StyleFactory {
  private readonly styles = new Map<string, GlyphStyle>();

  get(font: string): GlyphStyle {
    const existing = this.styles.get(font);
    if (existing) {
      return existing;
    }
    const created = new GlyphStyle(font);
    this.styles.set(font, created);
    return created;
  }
}

const factory = new StyleFactory();
const first = factory.get('mono-12');
const second = factory.get('mono-12');
console.log(first === second);
