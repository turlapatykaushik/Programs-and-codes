/*
* @turlapatykaushik
* github url : github.com/turlapatykaushik
* problem description : Find point which is symmetric to point p about q
*/

#include<iostream>
#include<string>
using namespace std;
int main()
{
int t;
cin >> t;
while (t--)
{
int px, py, qx, qy;
cin >> px >> py >> qx >> qy;
cout << 2 * qx - px << " " << 2 * qy - py << endl;
}
return 0;
}
