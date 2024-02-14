

#ifndef DEFINITIONS_H_
#define DEFINITIONS_H_

//Structure for a word node
typedef struct word{
	char *cp;
	int LetterCount;
	int position;
	struct word *next;
}WORD;
//Structure for sentence node
typedef struct sentence {
	struct word *wp;
	int lineCount;
	int WordCount;
	struct sentence *next;
}SENTENCE;
//Structure for the linked list
typedef struct linkedList{
	SENTENCE *first;
	int total;
}Llist;

#endif
