#include <iostream>
#include <memory>

struct Image {
    virtual ~Image() = default;
    virtual void display() = 0;
};

class RealImage : public Image {
public:
    RealImage() {
        std::cout << "load image\n";
    }

    void display() override {
        std::cout << "display image\n";
    }
};

class ImageProxy : public Image {
public:
    void display() override {
        if (!real_) {
            real_ = std::make_unique<RealImage>();
        }
        real_->display();
    }

private:
    std::unique_ptr<RealImage> real_;
};

int main() {
    ImageProxy proxy;
    proxy.display();
    proxy.display();
}
