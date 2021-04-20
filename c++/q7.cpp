#include <iostream>
using namespace std;
class complex
{
public:
    int real, imaj;
    complex(int x, int y)
    {
        real = x;
        imaj = y;
    }
};

int main()
{
    int real1, imaj1, real2, imaj2;
    cout << "enter the first real num ";
    cin >> real1;
    cout << "enter the first imaj num ";
    cin >> imaj1;
    cout << "enter the second real num ";
    cin >> real2;
    cout << "enter the second imaj num ";
    cin >> imaj2;

    complex num1(real1, imaj1);
    complex num2(real2, imaj2);

    cout << "the sum of the real parts is " << num1.real + num2.real << endl;
    cout << "the sum of the imaj parts is " << num1.imaj + num2.imaj << endl;
    return 0;
}
