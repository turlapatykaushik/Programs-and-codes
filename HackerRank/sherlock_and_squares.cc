#include <cmath>
#include <cstdio>
#include<string>
#include<math.h>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    long long int A,B,testcase;
    cin >> testcase;
    for(long long int p = 0; p < testcase;p++){
       long long int count = 0;
        cin >> A >> B;
        int rB = (int) floor(sqrt(B));
        int rA = (int) ceil(sqrt(A));
        cout<< (rB-rA + 1) << endl; 
    }
    return 0;
    }
