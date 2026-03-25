#include <iostream>

class DataProcessor {
public:
    virtual ~DataProcessor() = default;
    
    void process() {
        readData();
        parseData();
        writeData();
    }
    
protected:
    virtual void readData() = 0;
    virtual void parseData() = 0;
    virtual void writeData() = 0;
};

class CSVProcessor : public DataProcessor {
protected:
    void readData() override {
        std::cout << "Reading CSV data\n";
    }
    
    void parseData() override {
        std::cout << "Parsing CSV\n";
    }
    
    void writeData() override {
        std::cout << "Writing processed CSV\n";
    }
};

class JSONProcessor : public DataProcessor {
protected:
    void readData() override {
        std::cout << "Reading JSON data\n";
    }
    
    void parseData() override {
        std::cout << "Parsing JSON\n";
    }
    
    void writeData() override {
        std::cout << "Writing processed JSON\n";
    }
};

int main() {
    CSVProcessor csv;
    csv.process();
    
    JSONProcessor json;
    json.process();
}
