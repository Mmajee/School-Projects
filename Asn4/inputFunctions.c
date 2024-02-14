

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "definitions.h"
#include "headers.h"

void inputString(SENTENCE **line, char str[], int *size){
	int i = 0, j, c, w, pos; //iterative variables and position of a word variable

	do {
			//Get the input
			printf("Enter a string: ");
			fgets(str, 1000, stdin);

			//If there is not input, exit the function
			if (strcmp(str, "\n") == 0){
				break;
			}

			(*line) = (SENTENCE *) realloc((*line), (i + 1) * sizeof(SENTENCE)); //allocate memory for another line of input

			w = 0;

			(*line)[i].lineCount= i + 1;
			(*size)++;
			(*line)[i].wp = (WORD *)calloc(1, sizeof(WORD)); //allocate memory for WORD structure
			(*line)[i].wp[w].cp = (char *) calloc(1, sizeof(char)); //Allocate memory to store the single words

			j = 0;
			c = 0;
			pos = 1;
			while (str[j]){

				//If we have reached the end of a single word, add a terminating character to the dynamic char array
				//and fill in the lettercount, position, and increase the wordcount.
				if (str[j] != ' ' && str[j + 1] == ' '){
					(*line)[i].wp[w].cp[c] = str[j];
					c++;
					(*line)[i].wp[w].LetterCount = c;
					(*line)[i].wp[w].position = pos;
					(*line)[i].WordCount = pos;
					pos++;
					(*line)[i].wp[w].cp = (char *) realloc((*line)[i].wp[w].cp, (c + 1) * sizeof(char));
					(*line)[i].wp[w].cp[c] = '\0';
					w++;
				//If the current character is a letter, allocate memory for it and store it
				} else if (str[j] != ' ' && str[j] != '\0' && str[j] != '\n'){
					(*line)[i].wp[w].cp[c] = str[j];
					(*line)[i].wp[w].cp = (char *) realloc((*line)[i].wp[w].cp, (c + 2) * sizeof(char));
					c++;
					(*line)[i].wp[w].LetterCount = c;
				//If we have encountered the beginning of another word, make another WORD structure and char array
				}else if(str[j] == ' ' && str[j + 1] != ' ' && str[j + 1] != '\n' && str[j + 1] != '\0'){
					(*line)[i].wp = (WORD *) realloc((*line)[i].wp, (w + 1) * sizeof(WORD));
					(*line)[i].wp[w].cp = (char *) calloc(1, sizeof(char));
					c = 0;
				//If we have reached the end of the current input, add termininating character to the char array and
				//fill in the current WORD structure with the position, letter count, and Word count.
				} else if ((str[j] == '\n' || str[j] == '\0') && str[j - 1] != ' '){
					(*line)[i].wp[w].cp = (char *) realloc((*line)[i].wp[w].cp, (c + 1) * sizeof(char));
					c++;
					(*line)[i].wp[w].LetterCount = c;
					(*line)[i].wp[w].cp[c] = '\0';
					(*line)[i].wp[w].position = pos;
					(*line)[i].WordCount = pos;
					pos++;
				}

				j++;
			}

			i++;
			w = 0;

		} while(1);
}
