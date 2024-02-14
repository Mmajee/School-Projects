

#ifndef DEFINITIONS_H_
#define DEFINITIONS_H_

typedef struct word{
	char *cp;
	int LetterCount;
	int position;
}WORD;

typedef struct sentence {
	struct word *wp;
	int lineCount;
	int WordCount;
}SENTENCE;

#endif
