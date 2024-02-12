package cp213;

import java.util.Scanner;

public class Decipher {
	public static final String ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	public static final int ALPHA_LENGTH = ALPHA.length();
	public static void main(String[] args) {
		final String CIPHERTEXT = "AVIBROWNZCEFGHJKLMPQSTUXYD";
	//for testing substitute method
			// test code here
		Scanner keyboard = new Scanner(System.in);
		
		
		String s = "";
		int n = 0;
		String Sshift = "";
		String Ssub = "";
		
		System.out.print("Enter a cipher string: ");
		s = keyboard.nextLine();
		System.out.print("Enter a shift length: ");
		n = keyboard.nextInt();	
		keyboard.close();
		Sshift = Decipher.shift(s, n);
		System.out.println("Plain text for shift: " + Sshift);
		Ssub = Decipher.substitute(s, CIPHERTEXT);
		System.out.print("Plain text for substitute: " + Ssub);
		
		}
		
		/** Decipher a string using a shift cipher.
		 * @param s
		 *            string to decipher
		 * @param n
		 *            the number of letters to shift
		 * @return the original plaintext string
		 */
		public static String shift(String s, int n) {
			// method code here
			String Sshift = "";
			int j = 0;
			int k = 0;
			
			String s2 = s.toUpperCase();
			
			for (int i = 0; i < s2.length(); i++) {
				
				if (Character.isLetter(s2.charAt(i))) {
					j = ALPHA.indexOf(s2.charAt(i));
					
					k = j - n;
					if (k < 0) {
						k = k + 26;
					}
					Sshift += ALPHA.charAt(k);
				}
				else {
					Sshift += s.charAt(i);
					}
				
			}
			
			return Sshift;
			
			}
			
			/**
			 * Decipher a string using the letter positions in ciphertext.
			 * 
			 * @param s
			 *            string to decipher
			 * @param ciphertext*            ciphertext alphabet
			 * @return the plaintextstring
			 */
		public static String substitute(String s, String ciphertext) {
			// method code here
			String Ssub = "";
			int j = 0;
			String s2 = s.toUpperCase();
			
			for (int i = 0; i < s2.length(); i++) {
				j = ciphertext.indexOf(s2.charAt(i));
				
				if (Character.isLetter(s2.charAt(i))) {
					Ssub += ALPHA.charAt(j);
				}
				else {
					Ssub += s2.charAt(i);
				}
			}
			
			return Ssub;
			
		}
		
	}
	

