#include <iostream>
#include <vector>
#include <memory>

template <typename T>
class Iterator {
public:
    virtual ~Iterator() = default;
    virtual bool hasNext() = 0;
    virtual T next() = 0;
};

template <typename T>
class Collection {
public:
    virtual ~Collection() = default;
    virtual std::unique_ptr<Iterator<T>> createIterator() = 0;
};

template <typename T>
class ArrayIterator : public Iterator<T> {
private:
    std::vector<T>& items;
    int position = 0;
public:
    ArrayIterator(std::vector<T>& items) : items(items) {}
    
    bool hasNext() override {
        return position < items.size();
    }
    
    T next() override {
        return items[position++];
    }
};

template <typename T>
class ArrayCollection : public Collection<T> {
private:
    std::vector<T> items;
public:
    void add(T item) { items.push_back(item); }
    
    std::unique_ptr<Iterator<T>> createIterator() override {
        return std::make_unique<ArrayIterator<T>>(items);
    }
};

int main() {
    ArrayCollection<int> collection;
    collection.add(10);
    collection.add(20);
    collection.add(30);
    
    auto it = collection.createIterator();
    while (it->hasNext()) {
        std::cout << it->next() << " ";
    }
    std::cout << std::endl;
}
