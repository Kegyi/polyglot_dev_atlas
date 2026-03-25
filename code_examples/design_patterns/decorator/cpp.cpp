#include <iostream>
#include <memory>
#include <string>

struct Notifier {
    virtual ~Notifier() = default;
    virtual void send(const std::string& message) const = 0;
};

struct EmailNotifier : Notifier {
    void send(const std::string& message) const override {
        std::cout << "email: " << message << '\n';
    }
};

class NotifierDecorator : public Notifier {
public:
    explicit NotifierDecorator(std::unique_ptr<Notifier> inner) : inner_(std::move(inner)) {}

protected:
    std::unique_ptr<Notifier> inner_;
};

class SmsDecorator : public NotifierDecorator {
public:
    using NotifierDecorator::NotifierDecorator;

    void send(const std::string& message) const override {
        inner_->send(message);
        std::cout << "sms: " << message << '\n';
    }
};

int main() {
    auto notifier = std::make_unique<SmsDecorator>(std::make_unique<EmailNotifier>());
    notifier->send("deployment done");
}
