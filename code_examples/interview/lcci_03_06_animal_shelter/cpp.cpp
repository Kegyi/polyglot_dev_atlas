#include <iostream>
#include <queue>
#include <string>

struct Animal {
    int id;
    std::string type;
    int order;
};

class AnimalShelter {
public:
    AnimalShelter() : ticket(0) {}

    void enqueue(const Animal& a) {
        Animal withOrder = a;
        withOrder.order = ticket++;
        if (withOrder.type == "dog") {
            dogs.push(withOrder);
        } else {
            cats.push(withOrder);
        }
    }

    int dequeueAny() {
        if (dogs.empty() && cats.empty()) return -1;
        if (dogs.empty()) return dequeueCat();
        if (cats.empty()) return dequeueDog();
        if (dogs.front().order < cats.front().order) return dequeueDog();
        return dequeueCat();
    }

    int dequeueDog() {
        if (dogs.empty()) return -1;
        int id = dogs.front().id;
        dogs.pop();
        return id;
    }

    int dequeueCat() {
        if (cats.empty()) return -1;
        int id = cats.front().id;
        cats.pop();
        return id;
    }

private:
    int ticket;
    std::queue<Animal> dogs;
    std::queue<Animal> cats;
};

int main() {
    AnimalShelter shelter;
    shelter.enqueue({1, "dog", 0});
    shelter.enqueue({2, "cat", 0});
    shelter.enqueue({3, "dog", 0});
    std::cout << shelter.dequeueAny() << '\n';
    std::cout << shelter.dequeueCat() << '\n';
    std::cout << shelter.dequeueDog() << '\n';
    std::cout << shelter.dequeueAny() << '\n';
    return 0;
}
