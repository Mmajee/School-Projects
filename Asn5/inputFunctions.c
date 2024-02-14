

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "definitions.h"
#include "headers.h"

void inputString(Llist *list, char str[]){
	int i = 0, j, c, pos; //iterative variables and position of a word variable

	SENTENCE *line;
	WORD *wptr;
	char word[100];

	do {
			//Get the input
			printf("Enter a string: ");
			fgets(str, 1000, stdin);

			//If there is not input, exit the function
			if (strcmp(str, "\n") == 0){
				break;
			}

			line = createSentenceNode(i + 1); //Create a sentece node for the current line of input
			insertSentence(list, line); //Insert the sentece node into the linked list
			list->total++;

			j = 0;
			c = 0;
			pos = 1;
			while (str[j]){
				//If we have reached the end of a single word, add a terminating character to end of the word to store
				//and creat a word node then added to the sentence list.
				if (str[j] != ' ' && str[j + 1] == ' '){
					word[c] = str[j];
					c++;
					wptr = createWordNode(word, c, pos);
					line->WordCount = pos;
					pos++;
					insertWordNode(list, wptr);
				//If the current character is a letter, add it to the word that will be used to create a word node
				} else if (str[j] != ' ' && str[j] != '\0' && str[j] != '\n'){
					word[c] = str[j];
					c++;
				//If we have encountered the beginning of another word, set the character iterative variable to 0
				}else if(str[j] == ' ' && str[j + 1] != ' ' && str[j + 1] != '\n' && str[j + 1] != '\0'){
					c = 0;
				//If we have reached the end of the current input, create a word node and store it in the list of sentences.
				} else if ((str[j] == '\n' || str[j] == '\0') && str[j - 1] != ' '){
					wptr = createWordNode(word, c, pos);
					line->WordCount = pos;
					pos++;
					insertWordNode(list, wptr);
				}

				j++;
			}

			i++;

		} while(1);
}

//Function to insert a word node into a sentence
void insertWordNode(Llist *list, WORD *node){
	SENTENCE *ptr;
	SENTENCE *prev;
	WORD *wptr;
	WORD *wprev;
	int i = 0;


	ptr = list->first;
	wprev = NULL;

	//Find the latest Sentence inserted into the list
	while (i < list->total){
		prev = ptr;
		ptr = ptr->next;
		i++;
	}

	wptr = prev->wp;
	wprev = NULL;
	//Find the end of the word list
	while (wptr != NULL){
		wprev = wptr;
		wptr = wptr->next;
	}


	if (wprev == NULL){
		prev->wp = node; //If the list is empty, the current word is the first node in the linked list
	} else {
		wprev->next = node; //If it is not empty, add the current word to the end of the list
	}


}
//Function to insert a Sentence into the linked list
void insertSentence(Llist *list, SENTENCE *line){
	SENTENCE *ptr;
	SENTENCE *prev;

	prev = NULL;
	ptr = list->first;
	//Find the end of the linked list
	while (ptr != NULL){
		prev = ptr;
		ptr = ptr->next;
	}

	if (prev == NULL){
		list->first = line; //If the list is empty, the current sentence is set as the first
	} else {
		prev->next = line; //Otherwise add it to the end
	}

}
