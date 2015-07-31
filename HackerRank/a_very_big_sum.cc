#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    long int sizeofarray;
    long int a[10];
    long int i;
   /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
   cin >> sizeofarray;
for ( i = 0; i < sizeofarray; ++i)
{
    cin >> a[i];
}
    long int sum = 0;
    for(i =0;i<sizeofarray;i++)
        {
        sum = sum + a[i];
    }
    cout << sum << endl;
    return 0;
}
