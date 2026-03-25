#include <iostream>
#include <string>
#include <utility>
#include <vector>

struct Report {
    std::string title;
    std::vector<std::string> sections;
};

class ReportBuilder {
public:
    ReportBuilder& title(std::string value) {
        report_.title = std::move(value);
        return *this;
    }

    ReportBuilder& section(std::string value) {
        report_.sections.push_back(std::move(value));
        return *this;
    }

    Report build() {
        return report_;
    }

private:
    Report report_;
};

int main() {
    Report report = ReportBuilder()
        .title("Daily Build")
        .section("tests: green")
        .section("deploy: staged")
        .build();

    std::cout << report.title << '\n';
    for (const auto& section : report.sections) {
        std::cout << "- " << section << '\n';
    }
}