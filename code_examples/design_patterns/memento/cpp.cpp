#include <iostream>
#include <string>
#include <vector>
#include <memory>

class Memento {
private:
    std::string state;
public:
    Memento(const std::string& s) : state(s) {}
    std::string getState() const { return state; }
};

class Originator {
private:
    std::string state;
public:
    void setState(const std::string& s) { state = s; }
    std::string getState() const { return state; }
    
    std::shared_ptr<Memento> saveState() {
        return std::make_shared<Memento>(state);
    }
    
    void restoreState(const std::shared_ptr<Memento>& memento) {
        state = memento->getState();
    }
};

class Caretaker {
private:
    std::vector<std::shared_ptr<Memento>> history;
public:
    void save(std::shared_ptr<Memento> memento) {
        history.push_back(memento);
    }
    
    std::shared_ptr<Memento> restore(int index) {
        if (index >= 0 && index < history.size()) {
            return history[index];
        }
        return nullptr;
    }
};

int main() {
    Originator originator;
    Caretaker caretaker;
    
    originator.setState("State 1");
    caretaker.save(originator.saveState());
    
    originator.setState("State 2");
    caretaker.save(originator.saveState());
    
    originator.setState("State 3");
    std::cout << "Current: " << originator.getState() << std::endl;
    
    originator.restoreState(caretaker.restore(0));
    std::cout << "Restored: " << originator.getState() << std::endl;
}
