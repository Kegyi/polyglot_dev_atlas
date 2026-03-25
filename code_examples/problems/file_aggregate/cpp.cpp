#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <numeric>
#include <algorithm>
#include <future>
#include <stdexcept>
#include <optional>

struct Record {
    std::string name;
    int score;
};

class FileProcessor {
public:
    explicit FileProcessor(const std::string& path) : path_(path) {}
    std::vector<Record> readAll() const {
        std::ifstream in(path_);
        if (!in) throw std::runtime_error("unable to open file");
        std::vector<Record> out;
        std::string line;
        while (std::getline(in, line)) {
            if (line.empty() || line[0] == '#') continue;
            if (auto r = parseLine(line)) out.push_back(*r);
        }
        return out;
    }
private:
    std::string path_;
    static std::optional<Record> parseLine(const std::string& line) {
        std::istringstream iss(line);
        std::string name;
        int score;
        if (!std::getline(iss, name, ',')) return std::nullopt;
        if (!(iss >> score)) return std::nullopt;
        return Record{ name, score };
    }
};

static double average(const std::vector<int>& v) {
    if (v.empty()) return 0.0;
    return std::accumulate(v.begin(), v.end(), 0.0) / v.size();
}

int main(int argc, char** argv) {
    try {
        const std::string path = (argc > 1) ? argv[1] : "data.txt";
        FileProcessor fp(path);
        auto records = fp.readAll();

        std::map<std::string, std::vector<int>> buckets;
        for (const auto& r : records) buckets[r.name].push_back(r.score);

        std::vector<std::future<std::pair<std::string, double>>> futures;
        for (const auto& p : buckets) {
            auto name = p.first;
            auto scores = p.second;
            futures.push_back(std::async(std::launch::async,
                [name, scores]() {
                    return std::make_pair(name,
                        average(scores));
                }));
        }

        std::vector<std::pair<std::string, double>> results;
        for (auto& f : futures) results.push_back(f.get());

        std::sort(results.begin(), results.end(),
            [](const auto& a, const auto& b){ return a.second > b.second; });

        for (const auto& r : results) {
            std::cout << r.first << ": " << r.second << std::endl;
        }
    } catch (const std::exception& ex) {
        std::cerr << "Error: " << ex.what() << std::endl;
        return 1;
    }
    return 0;
}
