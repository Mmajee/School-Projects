package cp213;

import java.util.Scanner;

public class ValidDeclaration{
	
	public static void main(String args[]) {
		// test code here
		
		Scanner keyboard = new Scanner(System.in);
		
		String statement = "";
		
		System.out.print("Enter a string: ");
		statement = keyboard.nextLine();
		
		keyboard.close();
		
		if (ValidDeclaration.isValid(statement) == true) {
			System.out.print("'" + statement + "' is a valid Java variable definition.");
		}
		else {
			System.out.print("'" + statement + "' is not a valid Java variable definition.");
		}
		
		}
	
	/** Determines if the given string is a valid Java variable
	 * definition of the form “dataType variableName;”.
	 *Variables names must start with a letter or an underscore, but 
	 * cannot be an underscore alone.The rest of the variable name 
	 *may consist of letters, numbers andunderscores.Permitted data 
	 * types are byte, short, char, int, long, float, double and 
	 * boolean.The statement must terminate at ‘;’.
	 * @param statement
	 *            a string to test as a Java statement
	 * @return true if statement is a valid Java statement, false 
	 * otherwise
	 */
	public static boolean isValid(final String statement) {
		// method code here
		
		int j = 0;
		String s1 = "";
		String s2 = "";
		
		
		
		while ((j < statement.length()) && (statement.charAt(j) != ' ') ) {
			s1 += statement.charAt(j);
			//System.out.println(s1); 
			j += 1;
		}
		
		//System.out.println("HO"); 
		while (j < statement.length()) {
			if (statement.charAt(j) != ' ') {
				s2 += statement.charAt(j);
				}
			j += 1;
			}
		
		
		
		
		if (s2.equals("")) {
			return false;
		
		}
		
				
		else if ((!s1.equals("byte")) && (!s1.equals("short")) && (!s1.equals("char")) && (!s1.equals("int")) && (!s1.equals("long")) && (!s1.equals("float")) && (!s1.equals("double")) && (!s1.equals("boolean")) ) {
			return false;
		}
		
		else if (s2.charAt(s2.length() - 1) != ';') {
			
			return false;
		}
				
		else if ((s2.charAt(0) == '_') && (s2.length() == 1)) {
			return false;
		}
		
		else if ((Character.isLetter(s2.charAt(0)) == false) && (s2.charAt(0) != '_')) {
			return false;
		}
		else {
			return true;
		}
			
		
		}
	}

