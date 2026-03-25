#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class WordsFrequency {
public:
    explicit WordsFrequency(const vector<string>& book) {
        for (const string& word : book) {
            ++counter[word];
        }
    }

    int get(const string& word) const {
        auto it = counter.find(word);
        return it == counter.end() ? 0 : it->second;
    }

private:
    unordered_map<string, int> counter;
};

int main() {
    vector<string> book = {"i", "have", "an", "apple", "he", "have", "a", "pen"};
    WordsFrequency wf(book);
    cout << wf.get("have") << endl;
    cout << wf.get("you") << endl;
    return 0;
}
