

#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "definitions.h"
#include "headers.h"

//Function to create a word node
WORD* createWordNode(char word[], int letterCount, int position){
	//Allocate memory for another WORD structure
	WORD *node = (WORD*) malloc(sizeof(WORD));

	//Fill in the parameters
	node->LetterCount = letterCount;
	node->position = position;
	node->next = NULL;
	//Allocate memory for a dynamic char array
	node->cp = (char*) calloc(letterCount + 1, sizeof(char));

	strncpy(node->cp, word, letterCount);
	//Add the terminating character to the end of the word.
	node->cp[letterCount] = '\0';

	return node;
}
//Function to create a sentence node
SENTENCE* createSentenceNode(int lineNumber){
	SENTENCE *line = (SENTENCE *) malloc(sizeof(SENTENCE)); //allocate memory for another line of input
	//Fill in the parameters for the Sentence structure.
	line->WordCount = 0;
	line->lineCount = lineNumber;
	line->next = NULL;
	line->wp = NULL;

	return line;
}
