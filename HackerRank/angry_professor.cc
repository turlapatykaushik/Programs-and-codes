#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int test_case;
    cin >>test_case;
    while(test_case >0){
        int no_of_students, students_to_be_in,count = 0,number;
        cin >> no_of_students >> students_to_be_in ;
        test_case = test_case -1;
    for(int i = 0; i< no_of_students;i++){
        cin >> number;
        if(number <= 0){
            count+=1;
        }
    }
    if(count >= students_to_be_in){
        cout << "NO" << endl;
    }
    else{
        cout << "YES" << endl;
    }}
    return 0;
}
