#include <iostream>
using namespace std;

int main()
{
    int arr[4], max = 0;
    for (int i = 0; i < 4; i++)
    {
        cout << "enter the number " << i << " : ";
        cin >> arr[i];
    }
    max = arr[0];
    for (int i = 1; i < 4; i++)
    {
        if (arr[i] > max)
        {
            max = arr[i];
        }
    }
    cout << max << " is the lagest number";

    return 0;
}