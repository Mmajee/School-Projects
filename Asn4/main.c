

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "definitions.h"
#include "headers.h"

int main(){
	char str[1000]; //array for user input

	//SENTENCE structure to store the lines
	SENTENCE **line;
	line = (SENTENCE **) calloc(1, sizeof(SENTENCE));

	//Size variable to help iterate through the line dynamic array
	int size = 0;
	int *sp;
	sp = &size; //pointer for size is sent to the inputString function so size can be used in the output functions.

	inputString(line, str, sp);
	printf("\n");
	printWords(line, size);
	printf("\n");
	printLines(line, size);
	printf("\n");
	search(line, size, str);
	printf("END\n");
}


