

#include <stdio.h>
#include <stdlib.h>
#include "headers.h"

void deleteLine(Llist *list){
	char input;
	int num;
	SENTENCE *ptr;
	SENTENCE *prev;
	WORD *wptr;
	WORD *wprev;

	printf("Enter the number of the line you want to delete: ");

	//Scan for the number the user wants to delete
	scanf("%c", &input);

	while (input != '\n'){ //check if the input isn't empty

		num = input - '0'; //Convert the character to a number

		//Check if the number isn't larger than the amount of lines
		if (num > list->total){
			printf("ERROR: The number you have entered exceeds the number of lines\n");
		} else {
			ptr = list->first;
			prev = NULL;

			//Find the right line to delete
			while (ptr != NULL && ptr->lineCount != num){
				prev = ptr;
				ptr = ptr->next;
			}

			wptr = ptr->wp;

			if (num != 1){
				prev->next = ptr->next;
			} else {
				list->first = ptr->next;
			}

			//Free up all the word nodes in the sentence
			while (wptr != NULL){
				wprev = wptr;
				wptr = wptr->next;
				free(wprev->cp);
				free(wprev);
			}

			//Free the sentence memory
			free(ptr);

			if (num != 1){
				ptr = prev->next;
			} else {
				ptr = list->first;
			}

			//Go through the rest of the lines and update their line numbers
			while (ptr != NULL){
				ptr->lineCount--;
				ptr = ptr->next;
			}

			list->total--; //Decrease the total number of lines

			printLines(list); //Call the function printlines to show that the line is deleted

		}

		//Ask for input again
		printf("\n");
		printf("Enter the number of the line you want to delete: ");
		scanf("%c", &input);
		scanf("%c", &input);
	}

	ptr = list->first;

	//Free up all the dynamically allocated memory
	while (ptr != NULL) {
		prev = ptr->next;
		wptr = ptr->wp;
		while (wptr != NULL){
			wprev = wptr->next;
			free(wptr->cp);
			free(wptr);
			wptr = wprev;
		}
		free(ptr);
		ptr = prev;
	}

	free(list);
}
