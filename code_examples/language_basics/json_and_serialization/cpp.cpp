#include <iostream>
#include <sstream>
#include <string>

struct User {
    std::string name;
    int age;
};

std::string to_json(const User& user) {
    std::ostringstream out;
    out << "{\"name\":\"" << user.name << "\",\"age\":" << user.age << "}";
    return out.str();
}

std::string extract_name(const std::string& json) {
    const std::string needle = "\"name\":\"";
    auto start = json.find(needle);
    if (start == std::string::npos) {
        return "";
    }
    start += needle.size();
    auto end = json.find('"', start);
    if (end == std::string::npos) {
        return "";
    }
    return json.substr(start, end - start);
}

int main() {
    User user{"Alice", 29};
    std::string json = to_json(user);

    std::cout << "json: " << json << "\n";
    std::cout << "parsed name: " << extract_name(json) << "\n";
    return 0;
}
