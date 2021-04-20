#include <iostream>
using namespace std;

int main()
{
    int arr[3], sum = 0;
    for (int i = 0; i < 3; i++)
    {
        cin >> arr[i];
    }

    for (int i = 0; i < 3; i++)
    {
        sum = sum + arr[i];
    }
    cout << "the avg is " << sum / 3;

    return 0;
}