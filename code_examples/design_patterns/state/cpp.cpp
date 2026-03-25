#include <iostream>
#include <memory>

class State {
public:
    virtual ~State() = default;
    virtual void handle() = 0;
};

class StartState : public State {
public:
    void handle() override {
        std::cout << "Entering start state\n";
    }
};

class RunningState : public State {
public:
    void handle() override {
        std::cout << "Running state active\n";
    }
};

class StoppedState : public State {
public:
    void handle() override {
        std::cout << "Stopped state active\n";
    }
};

class Context {
private:
    std::shared_ptr<State> state;
public:
    void setState(std::shared_ptr<State> s) { state = s; }
    void request() { state->handle(); }
};

int main() {
    Context ctx;
    
    ctx.setState(std::make_shared<StartState>());
    ctx.request();
    
    ctx.setState(std::make_shared<RunningState>());
    ctx.request();
    
    ctx.setState(std::make_shared<StoppedState>());
    ctx.request();
}
