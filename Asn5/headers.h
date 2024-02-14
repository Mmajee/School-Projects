

#include "definitions.h"

#ifndef HEADERS_H_
#define HEADERS_H_

WORD* createWordNode(char word[], int letterCount, int position);
SENTENCE* createSentenceNode(int lineNumber);
void insertWordNode(Llist *list, WORD *node);
void insertSentence(Llist *list, SENTENCE *line);
void inputString(Llist *list, char str[]);
void printLines(Llist *list);
void search(Llist *list, char str[]);
void deleteLine(Llist *list);



#endif
