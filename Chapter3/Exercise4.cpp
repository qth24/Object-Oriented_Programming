#include <iostream>
#include <cstdlib>
#include <ctime>
#include <algorithm>
using namespace std;

class cArray {
    int *a;
    int n;

public:
    cArray(int size){
        n = size;
        a = new int[n];
        srand(time(0));
        for (int i = 0; i < n; i++){
            a[i] = rand() %201 - 100; // range -100 to 100
        }
    }

    ~cArray() {
        delete[] a;
    }

    void printarr() {
        for (int i = 0; i < n; i++)
        {
            cout << a[i] << " ";
        }
        cout << endl;
    }

    int max_neg() {
        int max = -101;
        for (int i = 0; i < n; i++)
        {
            if (a[i] < 0 && a[i] > max)
            {
                max = a[i];
            };
        }
        return max;
    }

    int freqx(int x){
        int count = 0;
        for (int i = 0; i < n; i++)
        {
            if (a[i] == x){count++;}
        }
        return count;
    }

    bool des_arr(){
        bool temp = true;
        for (int i = 1; i < n; i++)
        {
            if (a[i] > a[i-1]){temp = false; break;}
        }
        return temp;
    }

    void sortarr() {
    sort(a, a + n);
}
};

int main()
{
    cArray arr(15);
    cout << "> Initial array: ";
    arr.printarr();

    cout << "\n> Biggest negative number: " ;
    if (arr.max_neg() != -101){cout << arr.max_neg() << endl;} else {cout << "There is no negative number" << endl;}
    
    int dem;
    cout << "\n- Input the number need to be count: ";
    cin >> dem;
    cout << "> The frequency of " << dem << " is " << arr.freqx(dem) << " times" << endl;

    if (arr.des_arr() == true){cout << "\n> Descending array" << endl;} else {cout << "\n> Not descending array" << endl;}

    arr.sortarr();
    cout << "\n> Sorted array: "; 
    arr.printarr();

    return 0;
}