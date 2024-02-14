

/*
 * This program asks a user to enter an integer and adds up
 * all prime numbers excluding 1 up to that integer.
 * e.g. if the user enters 9, the prime numbers 2,3,5, and 7
 * are added for a total of 17.
 */

#include <stdio.h>
int main()
{
	int total,test,input,isprime;

	while(1) {
		total=0; //reset the total
		printf("Input? "); //asks for what integer to add up to
		scanf("%d",&input);

		if (input==0) break;

		//Loop to find and add the prime numbers
		for (int num=1; num<=input; num++){
			isprime = 0;

			//check if the number is prime
			for (test=2; test <= num; test++)
				if (num%test==0)
					isprime++;

			if (isprime==1)
				total = total + num; //add the prime number
		}

		printf("The final total is: %d\n",total);
	}
	return 0;
}


