#include <iostream>

using namespace std;

enum Mealtype{Regular,Medium,Large};
struct Passenger{
string name;
int age;
Mealtype mealtype; };

int main()
{
    Passenger newpass = { "Kaushik",20,Large };
    cout << newpass.name << endl;
    cout << newpass.age << endl;
    cout << newpass.mealtype << endl;
    return 0;
}
