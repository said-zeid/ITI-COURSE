#include <iostream>
using namespace std;
class said
{
public:
    int num1, num2;
    said(int x, int y)
    {
        num1 = x;
        num2 = y;
    }
};

int main()
{
    int x, y;
    cout << "enter the first number ";
    cin >> x;
    cout << "enter the second number ";
    cin >> y;

    said s(x, y);
    cout << "the sum is " << s.num1 + s.num2;
    return 0;
}
