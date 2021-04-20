#include <iostream>
using namespace std;

int main()
{
    int arr[5], *ptr;
    for (int i = 0; i < 5; i++)
    {
        cin >> arr[i];
    }
    ptr = arr;
    for (int i = 0; i < 5; i++)
    {
        cout << *ptr << endl;
        ptr++;
    }

    return 0;
}