#include <iostream>
#include <vector>
#include <memory>

class Observer {
public:
    virtual ~Observer() = default;
    virtual void update(const std::string& msg) = 0;
};

class Subject {
private:
    std::vector<std::shared_ptr<Observer>> observers;
public:
    void attach(std::shared_ptr<Observer> observer) {
        observers.push_back(observer);
    }
    
    void notify(const std::string& msg) {
        for (auto& obs : observers) {
            obs->update(msg);
        }
    }
};

class ConcreteObserver : public Observer {
private:
    std::string name;
public:
    ConcreteObserver(const std::string& n) : name(n) {}
    
    void update(const std::string& msg) override {
        std::cout << name << " received: " << msg << std::endl;
    }
};

int main() {
    auto subject = std::make_shared<Subject>();
    auto obs1 = std::make_shared<ConcreteObserver>("Observer1");
    auto obs2 = std::make_shared<ConcreteObserver>("Observer2");
    
    subject->attach(obs1);
    subject->attach(obs2);
    
    subject->notify("Event 1");
    subject->notify("Event 2");
}
