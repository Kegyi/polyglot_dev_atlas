#include <iostream>
#include <memory>
#include <numeric>
#include <vector>

struct Node {
    virtual ~Node() = default;
    virtual int totalSize() const = 0;
};

struct File : Node {
    explicit File(int size) : size_(size) {}
    int totalSize() const override { return size_; }
    int size_;
};

class Folder : public Node {
public:
    void add(std::unique_ptr<Node> child) {
        children_.push_back(std::move(child));
    }

    int totalSize() const override {
        int sum = 0;
        for (const auto& child : children_) {
            sum += child->totalSize();
        }
        return sum;
    }

private:
    std::vector<std::unique_ptr<Node>> children_;
};

int main() {
    auto root = std::make_unique<Folder>();
    root->add(std::make_unique<File>(5));
    auto sub = std::make_unique<Folder>();
    sub->add(std::make_unique<File>(7));
    sub->add(std::make_unique<File>(3));
    root->add(std::move(sub));
    std::cout << root->totalSize() << '\n';
}
