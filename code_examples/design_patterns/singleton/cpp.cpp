#include <iostream>
#include <string>

class Config {
public:
    static Config& instance() {
        static Config config;
        return config;
    }

    void setEnv(std::string value) {
        env_ = std::move(value);
    }

    const std::string& env() const {
        return env_;
    }

private:
    Config() = default;
    std::string env_ = "dev";
};

int main() {
    Config::instance().setEnv("prod");
    std::cout << Config::instance().env() << '\n';
}