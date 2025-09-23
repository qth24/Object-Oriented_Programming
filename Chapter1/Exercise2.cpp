#include <iostream>
using namespace std;

void func(int i, int j = 0) {
    cout << "So nguyen: " << i << " " << j << endl;
}

void func(float i = 0, float j = 0) {
    cout << "So thuc: " << i << " " << j << endl;
}

int main() {
    int i = 1, j = 2;
    float f = 1.5, g = 2.5;

    func();        // gọi hàm float mặc định
    func(i);       // gọi hàm int với i=1, j=0
    func(f);       // gọi hàm float với i=1.5, j=0
    func(i, j);    // gọi hàm int với i=1, j=2
    func(f, g);    // gọi hàm float với i=1.5, j=2.5

    return 0;
}
