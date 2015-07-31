#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<iomanip>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    float N;
    float positive = 0, negative = 0, zero = 0;
    float arr[100];
    cin >> N;
    for(int i =0;i < N;i++)
        {
        cin >> arr[i]; 
    }
    for(int j = 0;j < N;j++)
        {
        if(arr[j] > 0)
            {
            positive = positive + 1;
        }
        if(arr[j] == 0)
            {
            zero = zero+1;
        }
        if(arr[j]<0)
            {
            negative = negative + 1;
        }
    }
    float positive1 = positive/N;
    float negative1 = negative/N;
    float zero1 = zero/N;
    cout <<setprecision(3) << positive1 << endl;
    cout <<setprecision(3) << negative1 << endl;
    cout <<setprecision(3) << zero1 << endl;
    
    return 0;
}
