#include <deque>
#include <iostream>
#include <vector>

struct Node {
    int v;
    Node* l;
    Node* r;
    Node(int x): v(x), l(nullptr), r(nullptr) {}
};

void weave(std::deque<int> first, std::deque<int> second, std::vector<int> prefix,
           std::vector<std::vector<int>>& out) {
    if (first.empty() || second.empty()) {
        std::vector<int> merged = prefix;
        merged.insert(merged.end(), first.begin(), first.end());
        merged.insert(merged.end(), second.begin(), second.end());
        out.push_back(std::move(merged));
        return;
    }

    int h1 = first.front(); first.pop_front();
    auto p1 = prefix; p1.push_back(h1);
    weave(first, second, p1, out);

    int h2 = second.front(); second.pop_front();
    auto p2 = prefix; p2.push_back(h2);
    weave(first, second, p2, out);
}

std::vector<std::vector<int>> allSeq(Node* root) {
    if (!root) return { { } };

    auto leftSeq = allSeq(root->l);
    auto rightSeq = allSeq(root->r);
    std::vector<std::vector<int>> result;

    for (const auto& l : leftSeq) {
        for (const auto& r : rightSeq) {
            std::vector<std::vector<int>> weaved;
            weave(std::deque<int>(l.begin(), l.end()), std::deque<int>(r.begin(), r.end()), {root->v}, weaved);
            result.insert(result.end(), weaved.begin(), weaved.end());
        }
    }
    return result;
}

int main() {
    Node* root = new Node(2);
    root->l = new Node(1);
    root->r = new Node(3);

    auto ans = allSeq(root);
    for (const auto& seq : ans) {
        for (size_t i = 0; i < seq.size(); ++i) {
            std::cout << seq[i] << (i + 1 == seq.size() ? '\n' : ' ');
        }
    }
}
