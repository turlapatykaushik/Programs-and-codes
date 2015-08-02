#include <iostream> //Header
using namespace std;

int main() {
	int order_number; 
	
	cout << "Enter the order number"<<endl; 
	
	// stores the order number in the variable order_number
	cin >> order_number;
	
	if(order_number == 4){
		
		int with_rotations_and_reflections;
		int without_rotations_and_reflections;
		int fundamental_squares;
		int constant;
		
		// In its square about right angle rotation order
		int rotation_order_about_right_angle = 4;
		//Reflection in a diagonal order
		int reflection_order_in_diagonal = 2; 
		//Transformation by interchanging first and second row and column order
		int transformation_order_first_row_second_row_interchange = 2;
		//Transformation by interchaging middle two rows and two columns
		int transformation_order_middle_two_rows_interchange = 2;
		
		constant = (rotation_order_about_right_angle) * (reflection_order_in_diagonal) * (transformation_order_first_row_second_row_interchange) * (transformation_order_middle_two_rows_interchange);
		fundamental_squares = 31 + 71 +71 +47;
		with_rotations_and_reflections = fundamental_squares * constant;
		without_rotations_and_reflections = with_rotations_and_reflections / 8; // since a magic square has 8 rotations and reflections
		cout << "Total number of all magic squares which are unique i.e without rotations and reflections is "<< without_rotations_and_reflections<<endl;
		cout << "Total number of all magic squares i.e with rotations and reflections is "<< with_rotations_and_reflections<<endl;
	}
	return 0;
}
