#include <iostream>
#include <string>

class Person {
public:
    Person(std::string name, int age) : name_(std::move(name)), age_(age) {}

    std::string describe() const {
        return name_ + " is " + std::to_string(age_) + " years old";
    }

    void birthday() {
        ++age_;
    }

private:
    std::string name_;
    int age_;
};

int main() {
    Person person("Alice", 29);
    std::cout << person.describe() << "\n";
    person.birthday();
    std::cout << person.describe() << "\n";
    return 0;
}
