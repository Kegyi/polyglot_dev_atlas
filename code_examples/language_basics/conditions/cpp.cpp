#include <iostream>
#include <string>

std::string grade_to_label(int grade) {
    if (grade >= 90) {
        return "excellent";
    } else if (grade >= 75) {
        return "good";
    } else if (grade >= 60) {
        return "pass";
    }
    return "fail";
}

int main() {
    const int grade = 82;
    const int code = 2;

    std::cout << "if/else result: " << grade_to_label(grade) << "\n";

    switch (code) {
        case 1:
            std::cout << "switch: created\n";
            break;
        case 2:
            std::cout << "switch: updated\n";
            break;
        case 3:
            std::cout << "switch: deleted\n";
            break;
        default:
            std::cout << "switch: unknown\n";
            break;
    }

    bool ready = grade >= 60;
    std::cout << "ternary: " << (ready ? "can continue" : "needs retry") << "\n";
    return 0;
}
