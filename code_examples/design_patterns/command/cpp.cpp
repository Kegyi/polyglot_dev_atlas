#include <iostream>
#include <memory>
#include <vector>

class Receiver {
public:
    void turnOn() { std::cout << "Device is ON\n"; }
    void turnOff() { std::cout << "Device is OFF\n"; }
};

class Command {
public:
    virtual ~Command() = default;
    virtual void execute() = 0;
};

class TurnOnCommand : public Command {
private:
    std::shared_ptr<Receiver> receiver;
public:
    TurnOnCommand(std::shared_ptr<Receiver> r) : receiver(r) {}
    void execute() override { receiver->turnOn(); }
};

class TurnOffCommand : public Command {
private:
    std::shared_ptr<Receiver> receiver;
public:
    TurnOffCommand(std::shared_ptr<Receiver> r) : receiver(r) {}
    void execute() override { receiver->turnOff(); }
};

class Invoker {
private:
    std::vector<std::shared_ptr<Command>> commands;
public:
    void addCommand(std::shared_ptr<Command> cmd) { commands.push_back(cmd); }
    void executeAll() {
        for (auto& cmd : commands) {
            cmd->execute();
        }
    }
};

int main() {
    auto device = std::make_shared<Receiver>();
    auto invoker = std::make_unique<Invoker>();
    
    invoker->addCommand(std::make_shared<TurnOnCommand>(device));
    invoker->addCommand(std::make_shared<TurnOffCommand>(device));
    
    invoker->executeAll();
}
