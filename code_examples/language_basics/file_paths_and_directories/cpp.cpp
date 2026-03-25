#include <filesystem>
#include <iostream>

int main() {
    namespace fs = std::filesystem;

    fs::path base = "demo_folder";
    fs::path file_path = base / "sub" / "data.txt";

    fs::create_directories(file_path.parent_path());

    std::cout << "file path: " << file_path.string() << "\n";
    std::cout << "parent path: " << file_path.parent_path().string() << "\n";
    std::cout << "directory exists: " << fs::exists(file_path.parent_path()) << "\n";
    return 0;
}
