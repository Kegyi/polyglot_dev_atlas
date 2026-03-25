#include <iostream>
#include <memory>
#include <string>

struct Sender {
    virtual ~Sender() = default;
    virtual void send(const std::string& message) const = 0;
};

struct EmailSender : Sender {
    void send(const std::string& message) const override {
        std::cout << "email: " << message << '\n';
    }
};

struct SmsSender : Sender {
    void send(const std::string& message) const override {
        std::cout << "sms: " << message << '\n';
    }
};

class Notification {
public:
    explicit Notification(const Sender& sender) : sender_(sender) {}
    virtual ~Notification() = default;
    virtual void notify(const std::string& message) const = 0;

protected:
    const Sender& sender_;
};

class AlertNotification : public Notification {
public:
    using Notification::Notification;

    void notify(const std::string& message) const override {
        sender_.send("alert -> " + message);
    }
};

int main() {
    EmailSender email;
    SmsSender sms;
    AlertNotification(email).notify("CPU high");
    AlertNotification(sms).notify("CPU high");
}
