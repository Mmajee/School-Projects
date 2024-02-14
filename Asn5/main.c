

//gcc main.c createNode.c inputFunctions.c outputFunctions.c removeLine.c definitions.h headers.h -o Asn5

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "definitions.h"
#include "headers.h"

int main(){
	char str[1000]; //array for user input

	//SENTENCE structure to store the lines
	Llist *list = (Llist*) malloc(sizeof(Llist));
	list->total = 0;
	list->first = NULL;

	inputString(list, str);
	printf("\n");
	printLines(list);
	printf("\n");
	search(list, str);
	printf("\n");
	deleteLine(list);
	printf("END\n");
}


