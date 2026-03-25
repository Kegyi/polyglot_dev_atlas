#include <iostream>
#include <string>

struct Compiler {
    void run() const { std::cout << "compile\n"; }
};

struct TestRunner {
    void run() const { std::cout << "test\n"; }
};

struct Packager {
    void run() const { std::cout << "package\n"; }
};

class ReleaseFacade {
public:
    void deploy() const {
        compiler_.run();
        tests_.run();
        packager_.run();
    }

private:
    Compiler compiler_;
    TestRunner tests_;
    Packager packager_;
};

int main() {
    ReleaseFacade().deploy();
}
