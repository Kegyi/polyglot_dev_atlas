#include <iostream>
#include <memory>
#include <string>

struct Button {
    virtual ~Button() = default;
    virtual std::string render() const = 0;
};

struct Dialog {
    virtual ~Dialog() = default;
    virtual std::string render() const = 0;
};

struct WidgetFactory {
    virtual ~WidgetFactory() = default;
    virtual std::unique_ptr<Button> createButton() const = 0;
    virtual std::unique_ptr<Dialog> createDialog() const = 0;
};

struct LightButton : Button {
    std::string render() const override { return "light button"; }
};

struct LightDialog : Dialog {
    std::string render() const override { return "light dialog"; }
};

struct DarkButton : Button {
    std::string render() const override { return "dark button"; }
};

struct DarkDialog : Dialog {
    std::string render() const override { return "dark dialog"; }
};

struct LightFactory : WidgetFactory {
    std::unique_ptr<Button> createButton() const override { return std::make_unique<LightButton>(); }
    std::unique_ptr<Dialog> createDialog() const override { return std::make_unique<LightDialog>(); }
};

struct DarkFactory : WidgetFactory {
    std::unique_ptr<Button> createButton() const override { return std::make_unique<DarkButton>(); }
    std::unique_ptr<Dialog> createDialog() const override { return std::make_unique<DarkDialog>(); }
};

void showScreen(const WidgetFactory& factory) {
    auto button = factory.createButton();
    auto dialog = factory.createDialog();
    std::cout << button->render() << " + " << dialog->render() << '\n';
}

int main() {
    LightFactory light;
    DarkFactory dark;
    showScreen(light);
    showScreen(dark);
}