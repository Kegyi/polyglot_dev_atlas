#include <iostream>
#include <vector>
using namespace std;

class BinaryIndexedTree {
public:
    explicit BinaryIndexedTree(int n) : tree(n + 1, 0) {}

    void update(int index, int delta) {
        while (index < static_cast<int>(tree.size())) {
            tree[index] += delta;
            index += index & -index;
        }
    }

    int query(int index) const {
        int sum = 0;
        while (index > 0) {
            sum += tree[index];
            index -= index & -index;
        }
        return sum;
    }

private:
    vector<int> tree;
};

class StreamRank {
public:
    StreamRank() : bit(50010) {}

    void track(int x) {
        bit.update(x + 1, 1);
    }

    int getRankOfNumber(int x) const {
        return bit.query(x + 1);
    }

private:
    BinaryIndexedTree bit;
};

int main() {
    StreamRank streamRank;
    cout << streamRank.getRankOfNumber(1) << endl;
    streamRank.track(0);
    cout << streamRank.getRankOfNumber(0) << endl;
    return 0;
}
