

#include <stdio.h>

float recursive_exp(float base, int exp, float result);

int main(void) {
	float base;
	int exp; //The exponent variable
	float result;


	do{
		result = 1; //reset result to 1

		printf("Enter a base: (0 to quit)\n");
		scanf(" %f", &base);

		if (base == 0){ //If user enters 0, exit the loop.
			break;
		}

		printf("Enter an exponent:\n");
		scanf(" %d", &exp);

		result = recursive_exp(base, exp, result);

		printf("%f\n", result);


	} while (1);

	return 0;
}

float recursive_exp(float base, int exp, float result) {


	if (exp > 0 && exp % 2 == 0) { //calculate the result if the exp is even
		result = result * base * base;
		result = recursive_exp(base, exp - 2, result);
	} else if (exp > 0){ //calculate the result if the exp is odd
		result = result * base;
		result = recursive_exp(base, exp - 1, result);
	} else if (exp < 0 && exp % 2 == 0) { //calculate the result if the exp is even and negative
		result = result * (1 / base) * (1 / base);
		result = recursive_exp(base, exp + 2, result);
	} else if (exp < 0) { //calculate the result if the exp is odd and negative
		result = result * (1 / base);
		result = recursive_exp(base, exp + 1, result);
	} else {
		return result;
	}

	return result;

}
