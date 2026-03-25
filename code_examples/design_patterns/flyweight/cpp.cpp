#include <iostream>
#include <memory>
#include <string>
#include <unordered_map>

struct GlyphStyle {
    explicit GlyphStyle(std::string font) : font(std::move(font)) {}
    std::string font;
};

class StyleFactory {
public:
    const GlyphStyle* get(const std::string& font) {
        auto it = styles_.find(font);
        if (it == styles_.end()) {
            it = styles_.emplace(font, std::make_unique<GlyphStyle>(font)).first;
        }
        return it->second.get();
    }

private:
    std::unordered_map<std::string, std::unique_ptr<GlyphStyle>> styles_;
};

int main() {
    StyleFactory factory;
    const GlyphStyle* first = factory.get("mono-12");
    const GlyphStyle* second = factory.get("mono-12");
    std::cout << std::boolalpha << (first == second) << '\n';
}
