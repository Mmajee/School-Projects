
#include <stdio.h>
#include <string.h>

//Function Definitions
void print_array(int a[], int count);
void reverse_array(int a[], int count);
void find_min(int a[], int count);
void array_sum(int a[], int count);
void copy_array_reverse(int a[], int count);
void switch_first_last(int a[], int count);
void sort_array(int a[], int count);

int main(){

	int array[] = {12,63,44,89,3,55,73,27,37,18,1,99,50,22,45};

	int count = sizeof(array) / sizeof(array[0]); //Find number of elements in array
	int size = sizeof(array); //Determine the size of the array

	printf("Size of array: %d bytes\n", size);
	printf("Length of array: %d elements\n", count);

	printf("\n");
	printf("PART 1:\n");
	printf("The values stored in the array are:\n");
	print_array(array, count);

	printf("\n");
	printf("PART 2:\n");
	printf("The values stored in the array in reverse are:\n");
	reverse_array(array, count);

	printf("\n");
	printf("PART 3:\n");
	printf("The smallest value stored in the array is:\n");
	find_min(array, count);

	printf("\n");
	printf("PART 4:\n");
	printf("The sum (total) value of the array is:\n");
	array_sum(array, count);

	printf("\n");
	printf("PART 5:\n");
	printf("Copy the array into a new array, but in reverse order:\n");
	printf("Original array:\n");
	print_array(array, count);
	printf("New (Reversed) array: \n");
	copy_array_reverse(array, count);

	printf("\n");
	printf("PART 6:\n");
	printf("Switch the first value in the array with the last value in the array:\n");
	printf("Original array:\n");
	print_array(array, count);
	printf("Changed array: \n");
	switch_first_last(array, count);
	print_array(array, count);

	switch_first_last(array, count);

	printf("\n");
	printf("PART 7:\n");
	printf("Sort the array in ascending order:\n");
	printf("Original array:\n");
	print_array(array, count);
	printf("Changed array: \n");
	sort_array(array, count);
	print_array(array, count);

}

void print_array(int a[], int count){

	//prints every element in the array
	for (int i = 0; i < count; i++){
		printf("%5d", a[i]);
	}

	printf("\n");

}

void reverse_array(int a[], int count){

	//prints every element in the array in reverse
	for (int i = count - 1; i >= 0; i--){
		printf("%5d", a[i]);
	}

	printf("\n");
}

void find_min(int a[], int count){

	int min = a[0];
	int position;
	char string[3];
	int i;

	//Goes through every element in the array and finds the minimum value
	for (i = 0; i < count; i++){
		if (a[i] < min){
			min = a[i];
			position = i ; //keeps track of the position of the smallest element
		}
	}

	position = position + 1; //Add 1 sense position starts at 0

	//Find the ending for the position name
	if (position % 10 == 1 && position != 11){
		strcpy(string, "st");
	} else if (position % 10 == 2 && position != 12){
		strcpy(string, "nd");
	} else if (position % 10 == 3 && position != 13){
		strcpy(string, "rd");
	} else {
		strcpy(string, "th");
	}

	printf("value: %d at the %d%s position from the left\n", min, position, string);
}

//Calculates the sum of integers in the array
void array_sum(int a[], int count) {

	int sum = 0;

	for (int i = 0; i < count; i++){

		printf("%3d", a[i]);
		if (i != count - 1){
			printf(" +");
		}
		sum += a[i]; //Add the integer to the sum
	}

	printf(" equals: %d\n", sum);
}

//Copies an array into another in reverse
void copy_array_reverse(int a[], int count){

	int array2[count]; //create new array with same size as the original

	for (int i = count - 1; i >= 0; i--){
		array2[count - 1 - i] = a[i]; //The value at this position of the second array is
		                              //equal to the value at the same position + the number of
		                              //integers in the original array.
	}

	print_array(array2, count);
}

// Switched second and last element in an array
void switch_first_last(int a[], int count){
	int tmp; //Temperory variable to hold a value so its not lost
	tmp = a[0];
	a[0] = a[count - 1];
	a[count - 1] = tmp;
}

//Sorts the array in ascending order
void sort_array(int a[], int count){

	int tmp;

	for (int i = 0; i < count; i++){ //First loop goes through every integer.
		for(int j = i + 1; j < count; j++){ //Second loop compares the current integer with evey other integer in the array to check where it should be placed
			if (a[i] > a[j]){
				tmp = a[i];
				a[i] = a[j];
				a[j] = tmp;
			}
		}
	}
}
