#include <iostream>
#include <memory>
#include <string>
#include <vector>

class Speaker {
public:
    virtual ~Speaker() = default;
    virtual std::string speak() const = 0;
};

class Dog : public Speaker {
public:
    std::string speak() const override { return "woof"; }
};

class Cat : public Speaker {
public:
    std::string speak() const override { return "meow"; }
};

int main() {
    std::vector<std::unique_ptr<Speaker>> speakers;
    speakers.push_back(std::make_unique<Dog>());
    speakers.push_back(std::make_unique<Cat>());

    for (const auto& speaker : speakers) {
        std::cout << speaker->speak() << "\n";
    }
    return 0;
}
