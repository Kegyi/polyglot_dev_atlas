#include <iostream>
#include <vector>

// Draw a horizontal line from pixel x1 to x2 in a screen of 32-bit words per row.
// width is the number of pixels per row (multiple of 32).
std::vector<int> drawLine(int length, int w, int x1, int x2, int y) {
    int words_per_row = w / 32;
    std::vector<int> screen(length, 0);
    int offset = y * words_per_row;

    int start_byte = x1 / 32 + offset;
    int end_byte   = x2 / 32 + offset;
    int start_bit  = x1 % 32;
    int end_bit    = x2 % 32;

    for (int i = start_byte; i <= end_byte; i++) {
        int hi = (i == start_byte) ? (0xFF >> start_bit) : 0xFF;
        int lo = (i == end_byte)   ? ~(0xFF >> (end_bit + 1)) : 0xFF;
        screen[i] = hi & lo;
    }
    return screen;
}

int main() {
    // width=32, draw from x1=1 to x2=30 on row 0
    auto result = drawLine(1, 32, 1, 30, 0);
    // Print as hex
    for (int v : result) std::cout << std::hex << v << '\n';
}
