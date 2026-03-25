#include <iostream>
#include <string>
#include <vector>
using namespace std;

string below1000(int n) {
    vector<string> ones = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
    vector<string> teens = {"Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
    vector<string> tens = {"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};

    string s;
    if (n >= 100) {
        s += ones[n / 100] + " Hundred";
        n %= 100;
        if (n) s += " ";
    }
    if (n >= 20) {
        s += tens[n / 10];
        if (n % 10) s += " " + ones[n % 10];
    } else if (n >= 10) {
        s += teens[n - 10];
    } else if (n > 0) {
        s += ones[n];
    }
    return s;
}

string numberToWords(int num) {
    if (num == 0) return "Zero";
    if (num < 0) return "Negative " + numberToWords(-num);

    vector<string> units = {"", "Thousand", "Million", "Billion"};
    vector<string> parts;
    int unit = 0;
    while (num > 0) {
        int chunk = num % 1000;
        if (chunk > 0) {
            string piece = below1000(chunk);
            if (!units[unit].empty()) piece += " " + units[unit];
            parts.push_back(piece);
        }
        num /= 1000;
        ++unit;
    }

    string ans;
    for (int i = static_cast<int>(parts.size()) - 1; i >= 0; --i) {
        if (!ans.empty()) ans += " ";
        ans += parts[i];
    }
    return ans;
}

int main() {
    cout << numberToWords(123) << endl;
    cout << numberToWords(12345) << endl;
    cout << numberToWords(-1000010) << endl;
    return 0;
}
