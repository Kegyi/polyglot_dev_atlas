// Modern C++ Template Method using CRTP (Curiously Recurring Template Pattern)
// Compile-time polymorphism: no virtual dispatch, no vtable, concrete steps inlined.
#include <iostream>

template<typename Derived>
class DataProcessor {
public:
    void process() {
        derived().readData();
        derived().parseData();
        derived().writeData();
    }

private:
    Derived& derived() { return static_cast<Derived&>(*this); }
};

class CSVProcessor : public DataProcessor<CSVProcessor> {
public:
    void readData()  const { std::cout << "Reading CSV data\n"; }
    void parseData() const { std::cout << "Parsing CSV\n"; }
    void writeData() const { std::cout << "Writing processed CSV\n"; }
};

class JSONProcessor : public DataProcessor<JSONProcessor> {
public:
    void readData()  const { std::cout << "Reading JSON data\n"; }
    void parseData() const { std::cout << "Parsing JSON\n"; }
    void writeData() const { std::cout << "Writing processed JSON\n"; }
};

int main() {
    CSVProcessor csv;
    csv.process();

    JSONProcessor json;
    json.process();
}
