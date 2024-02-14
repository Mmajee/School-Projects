

#include <stdio.h>

int main(void)
{
  int choice; //The user input for what type of conversion to make
  char choice2; //The user input for which direction to make the conversion
  float value; //The value the user inputs to convert from
  float result;

  do{
     printf("What type of conversion do you want to make?\n");
     printf("1: Km <-> M\n");
     printf("2: L <-> gal\n");
     printf("3: cm <-> in\n");
     printf("4: Celsius <-> F\n");
     printf("5: Quit\n");
     scanf(" %d", &choice);

  if (choice == 5){ //If 5 is the input, exit the loop
	  break;
  } else if (choice == 1){
    do{
       printf("(K) Km->M; (M) M->Km\n"); //Which direction to make the conversion?
       scanf(" %c", &choice2);
     }while (choice2 != 'K' && choice2 != 'M'); //Loop only accepts one of the 2 choices
    
    printf("Enter a value:\n");
    scanf(" %f", &value);
    if (choice2 == 'K'){
      result = value * 0.62137; //Do the conversion
      printf("%f Km = %f M\n", value, result);   
    }else if (choice2 == 'M'){
      result = value / 0.62137;
      printf("%f M = %f Km\n", value, result); 
    }
  } else if (choice == 2){
    do{
       printf("(L) L->gal; (G) gal->L\n");
       scanf(" %c", &choice2);
    }while (choice2 != 'L' && choice2 != 'G');

    printf("Enter a value:\n");
    scanf(" %f", &value);
    if (choice2 == 'L'){
      result = value * 0.264172;
      printf("%f L = %f gal\n", value, result);   
    }else if (choice2 == 'G'){
      result = value / 0.264172;
      printf("%f gal = %f L\n", value, result); 
    }      
  } else if (choice == 3){
    do{
       printf("(C) cm->in; (I) in->cm\n");
       scanf(" %c", &choice2);
    }while (choice2 != 'C' && choice2 != 'I');

    printf("Enter a value:\n");
    scanf(" %f", &value);
    if (choice2 == 'C'){
      result = value * 0.393701;
      printf("%f cm = %f in\n", value, result);   
    }else if (choice2 == 'I'){
      result = value / 0.393701;
      printf("%f in = %f cm\n", value, result); 
    }
  } else {
    do{
       printf("(C) Celsius->F; (F) F->Celsius\n");
       scanf(" %c", &choice2);
    }while (choice2 != 'C' && choice2 != 'F'); 
    

    printf("Enter a value:\n");
    scanf(" %f", &value);
    if (choice2 == 'C'){
      result = value * ((float)9/(float)5) + 32;
      printf("%f Celsius = %f F\n", value, result);   
    }else if (choice2 == 'F'){
      result = (value - 32) * ((float)5/(float)9);
      printf("%f F = %f Celsius\n", value, result); 
    }
  }
 } while(1);

    
  
}
