#include <iostream>
using namespace std;

int main()
{
    int x, f = 0, reversed = 0;
    cin >> x;
    while (x != 0)
    {
        f = x % 10;
        reversed = reversed * 10 + f;
        x = x / 10;
    }
    cout << reversed;

    return 0;
}