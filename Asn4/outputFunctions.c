

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "headers.h"

void printWords(SENTENCE **line, int size){


	if (size != 0){ //Check if the SENTENCE structure is not empty
		int i = 0, w = 0;

		printf("This is all the words printed one at a time:\n");

		 while (i < size){

			 while (w < (*line)[i].WordCount){
				 printf("%s\n", (*line)[i].wp[w].cp);
				 w++;
			 }
			 w = 0;
			i++;
		}
	}


}

void printLines(SENTENCE **line, int size){

	if (size != 0){
		int i = 0, w = 0;

		printf("This is all the words printed on the same line as entered:\n");

		while (i < size){
			 while (w < (*line)[i].WordCount){
				 printf("%s", (*line)[i].wp[w].cp);
				 if (w != (*line)[i].WordCount - 1){
					 printf(" ");
				 }
				 w++;
			 }
			 printf("\n");
			 w = 0;
			i++;
		}
	}

}

void search(SENTENCE **line, int size, char str[]){

	if (size != 0){
		int i,w, found;

		do{

			printf("Enter a word to search for: ");
			gets(str);

			if (strcmp(str, "") == 0){
				break;
			}

			i = 0;
			w = 0;
			found = 0;

			 while (i < size){

				 while (w < (*line)[i].WordCount){

					 if (strcmp(str, (*line)[i].wp[w].cp) == 0){
						printf("%s found in line %d position %d\n", str, (*line)[i].lineCount, (*line)[i].wp[w].position);
						found = 1;
					 }
					 w++;
				 }
				 w = 0;
				i++;
			}

			//If the word is not found, print this message
			if (found == 0){
				printf("%s was not found\n", str);
			}

			printf("\n");

		}while (1);

		i = 0;
		w = 0;

		//Free up all the dynamically allocated memory
		while (i < size) {

			while (w < (*line)[i].WordCount){

				free((*line)[i].wp[w].cp);
				w++;
			}
			free((*line)[i].wp);
			w = 0;
			i++;
		}

		free(line);

	}

}

