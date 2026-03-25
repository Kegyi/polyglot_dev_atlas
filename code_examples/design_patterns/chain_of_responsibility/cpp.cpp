#include <iostream>
#include <memory>
#include <string>

class Request {
public:
    int level;
    std::string message;
    Request(int l, const std::string& m) : level(l), message(m) {}
};

class Handler {
protected:
    std::shared_ptr<Handler> next;
public:
    void setNext(std::shared_ptr<Handler> handler) { next = handler; }
    virtual void handle(const Request& req) = 0;
};

class LowLevelHandler : public Handler {
public:
    void handle(const Request& req) override {
        if (req.level <= 1) {
            std::cout << "LowLevelHandler: Processing " << req.message << std::endl;
        } else if (next) {
            next->handle(req);
        }
    }
};

class MidLevelHandler : public Handler {
public:
    void handle(const Request& req) override {
        if (req.level == 2) {
            std::cout << "MidLevelHandler: Processing " << req.message << std::endl;
        } else if (next) {
            next->handle(req);
        }
    }
};

class HighLevelHandler : public Handler {
public:
    void handle(const Request& req) override {
        if (req.level >= 3) {
            std::cout << "HighLevelHandler: Processing " << req.message << std::endl;
        }
    }
};

int main() {
    auto low = std::make_shared<LowLevelHandler>();
    auto mid = std::make_shared<MidLevelHandler>();
    auto high = std::make_shared<HighLevelHandler>();
    
    low->setNext(mid);
    mid->setNext(high);
    
    Request r1(1, "Simple request");
    Request r2(2, "Normal request");
    Request r3(3, "Critical request");
    
    low->handle(r1);
    low->handle(r2);
    low->handle(r3);
}
