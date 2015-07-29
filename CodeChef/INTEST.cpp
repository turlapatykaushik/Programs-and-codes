#include<iostream>

using namespace std;
int main()
{
int n , k, t;
int counter = 0;
cin >> n >> k;
for (int i = 0; i < n; i++)
{
    cin >> t;
    if(t % k == 0)
    {
        counter = counter +1;
    }
}
cout << counter << endl;
    return 0;
}
