/*
* @turlapatykaushik
* github url : github.com/turlapatykaushik
*/
#include<iostream>

using namespace std;

int main()
{
    int test_cases, total_numbers, sum = 0, count = 0;
    float average;
    cin >> test_cases;
    while(test_cases > 0)
    {
        test_cases = test_cases - 1;
        cin >> total_numbers;
        int arr[total_numbers];
        for(int i=0;i< total_numbers;i++)
        {
            cin >> arr[i];
			sum = sum + arr[i];
        }
        
        average = sum/total_numbers;
        for(int i=0; i < total_numbers;i++)
        {
            if(arr[i]>average)
            {
                count = count + 1;
            }
        }
            cout << count << endl;
            sum =0;
            count = 0;
        }
       
        return 0;
    }
