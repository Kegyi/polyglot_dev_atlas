#include <iostream>
#include <string>

struct Printer {
    virtual ~Printer() = default;
    virtual void print(const std::string& message) const = 0;
};

class JsonLogger {
public:
    void writeJson(const std::string& payload) const {
        std::cout << payload << '\n';
    }
};

class JsonLoggerAdapter : public Printer {
public:
    explicit JsonLoggerAdapter(const JsonLogger& logger) : logger_(logger) {}

    void print(const std::string& message) const override {
        logger_.writeJson("{\"message\":\"" + message + "\"}");
    }

private:
    const JsonLogger& logger_;
};

int main() {
    JsonLogger logger;
    JsonLoggerAdapter printer(logger);
    printer.print("build finished");
}
