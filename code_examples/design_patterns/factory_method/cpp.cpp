#include <iostream>
#include <memory>
#include <string>

struct Parser {
    virtual ~Parser() = default;
    virtual std::string parse() const = 0;
};

struct JsonParser : Parser {
    std::string parse() const override { return "parsed json"; }
};

struct CsvParser : Parser {
    std::string parse() const override { return "parsed csv"; }
};

class ImportJob {
public:
    virtual ~ImportJob() = default;
    std::string run() const {
        return createParser()->parse();
    }

private:
    virtual std::unique_ptr<Parser> createParser() const = 0;
};

class JsonImportJob : public ImportJob {
private:
    std::unique_ptr<Parser> createParser() const override { return std::make_unique<JsonParser>(); }
};

class CsvImportJob : public ImportJob {
private:
    std::unique_ptr<Parser> createParser() const override { return std::make_unique<CsvParser>(); }
};

int main() {
    JsonImportJob json;
    CsvImportJob csv;
    std::cout << json.run() << '\n';
    std::cout << csv.run() << '\n';
}