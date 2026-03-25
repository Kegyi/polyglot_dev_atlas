#include <iostream>
#include <memory>

class Mediator {
public:
    virtual ~Mediator() = default;
    virtual void notify(void* sender, const std::string& event) = 0;
};

class User {
protected:
    std::shared_ptr<Mediator> mediator;
    std::string name;
public:
    User(std::shared_ptr<Mediator> m, const std::string& n) : mediator(m), name(n) {}
    virtual ~User() = default;
    virtual void send(const std::string& msg) = 0;
    virtual void receive(const std::string& msg) = 0;
};

class ChatUser : public User {
public:
    using User::User;
    
    void send(const std::string& msg) override {
        std::cout << name << " sends: " << msg << std::endl;
        mediator->notify(this, msg);
    }
    
    void receive(const std::string& msg) override {
        std::cout << name << " receives: " << msg << std::endl;
    }
};

class ChatRoom : public Mediator {
private:
    std::shared_ptr<ChatUser> user1, user2;
public:
    void addUser(std::shared_ptr<ChatUser> u1, std::shared_ptr<ChatUser> u2) {
        user1 = u1;
        user2 = u2;
    }
    
    void notify(void* sender, const std::string& event) override {
        if (sender == user1.get()) {
            user2->receive(event);
        } else {
            user1->receive(event);
        }
    }
};

int main() {
    auto room = std::make_shared<ChatRoom>();
    auto u1 = std::make_shared<ChatUser>(room, "Alice");
    auto u2 = std::make_shared<ChatUser>(room, "Bob");
    
    room->addUser(u1, u2);
    
    u1->send("Hello!");
    u2->send("Hi there!");
}
