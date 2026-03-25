#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

bool isBalanced(const std::string& s) {
    static const std::unordered_map<char, char> closeToOpen = {
        {')', '('},
        {']', '['},
        {'}', '{'}
    };

    std::vector<char> st;
    st.reserve(s.size());

    for (char ch : s) {
        if (ch == '(' || ch == '[' || ch == '{') {
            st.push_back(ch);
        } else if (closeToOpen.count(ch)) {
            if (st.empty() || st.back() != closeToOpen.at(ch)) {
                return false;
            }
            st.pop_back();
        }
    }

    return st.empty();
}

int main() {
    const std::string input1 = "([{}])(()[]){}";
    const std::string input2 = "([)]";

    std::cout << std::boolalpha;
    std::cout << "input_1 valid: " << isBalanced(input1) << '\n';
    std::cout << "input_2 valid: " << isBalanced(input2) << '\n';
    return 0;
}
