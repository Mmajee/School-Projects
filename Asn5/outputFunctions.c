

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "headers.h"

void printLines(Llist *list){

	if (list && list->first != NULL){

		SENTENCE *ptr;
		WORD *wptr;
		ptr = list->first;
		int i;

		printf("This is all the words printed on the same line as entered:\n");

		//Iterate through each Sentence node in the list
		while (ptr != NULL){
			i = 0;
			wptr = ptr->wp;
			//Iterate through each word in the sentence list
			while (wptr != NULL){
				//Print the word and a space character until you reach the last word in the list.
				printf("%s", wptr->cp);
				if (i != ptr->WordCount - 1){
					printf(" ");
				}
				i++;
				wptr = wptr->next; //Go to next word in the list
			 }
			 printf("\n");
			 ptr = ptr->next; //Go to next sentence in the list
		}
	}

}

void search(Llist *list, char str[]){

	if (list && list->first != NULL){
		int found;
		SENTENCE *ptr;
		WORD *wptr;

		do{

			printf("Enter a word to search for: ");
			gets(str);

			if (strcmp(str, "") == 0){
				break;
			}

			ptr = list->first;
			found = 0;

			//Iterate through every sentence in the list
			 while (ptr != NULL){
				 wptr = ptr->wp;
				 //Iterate through each word in the sentece
				 while (wptr != NULL){
					 //If the word is the same as the user input, display the following message.
					 if (strcmp(str, wptr->cp) == 0){
						printf("%s found in line %d position %d\n", str, ptr->lineCount, wptr->position);
						found = 1;
					 }
					 wptr = wptr->next;
				 }
				 ptr = ptr->next;
			}

			//If the word is not found, print this message
			if (found == 0){
				printf("%s was not found\n", str);
			}

			printf("\n");

		}while (1);
	}

}

