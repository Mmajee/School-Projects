package cp213;

import java.util.Scanner;
import java.lang.StringBuilder;

public class SubPalindrome {
	
	public static void main(String[] args) {
	// test code here
	Scanner keyboard = new Scanner(System.in);
	
	String s = "";
	int minLen = 1;
	
	System.out.print("Enter a string of size 1-10 characters: ");
	s = keyboard.nextLine();
	SubPalindrome.testSubPalindromes(s, minLen);
	keyboard.close();
	
	}
	
		/** Determines and displays if any substrings of s are palindromes.
		 * The method tests all substrings of length minLen and more. If any
		 *  substrings are found to be palindromes, the message is displayed 
		 *  in the form "Following substring(s) of the string '...' are
		 *  palindrome(s): '..', '..'”. If none of the substrings are
		 *  palindrome, the output is:"No substrings of the string '..' are 
		 *  palindrome."
		 * @param s
		 *            a string
		 * @param minLen
		 *            an int
		 * @returns void
		 */
		public static void testSubPalindromes(final String s, int minLen) {
			// method code here
			
			String palindromes = "";
						
			if (s.length() < minLen) {
				System.out.println("'" + s + "'" + " is not a valid input, size less than 1");
				
			}
			else if (s.length() > 10) {
				System.out.println("'" + s + "'" + " is not a valid input, size more than 10");
			
				}	
			else {
				
				
				if (s.length() == 1) {
					System.out.print(" Following substring(s) of the string '" + s + "' are palindrome(s): ");
				}
			
				else {
					
					
					
					int start = 0;
					int j = 2;
					int incr = 2;
					
					while (incr <= s.length()) {
						
						while (j <= s.length()) {
							String s2 = s.substring(start, j);
							if (SubPalindrome.isPalindrome(s2)) {
								palindromes = palindromes + "'" + s2 + "'" + ", ";
								}
							start += 1;
							j += 1;
						}
						
						start = 0;
						incr += 1;
						j = incr;
	
			
					}
					
					if (palindromes.equals("") == false) {
						
						StringBuilder p = new StringBuilder(palindromes);
						
						p.deleteCharAt(p.length() - 2);
						
						
						
						palindromes = p.toString();
						
						System.out.print("Following substring(s) of the string '" + s + "' are palindrome(s): " + palindromes);
					}
					else {
						System.out.print("No substrings of the string " + "'" + s + "'" + " are palindromes.");
					}
				}
			}
			
			
		}
		/** Determines if s is a palindrome. Ignores case, spaces, digits,
		 * and punctuation in the string parameter s.
		 *
		 * @param s
		 *            a string
		 * @return true if s is a palindrome, false otherwise
		 */
		public static boolean isPalindrome(final String s) {
			// method code here

			int i = 0;
			
			StringBuilder str = new StringBuilder(s);
			
			
			while ( i < str.length()) {
				if (Character.isLetter(str.charAt(i)) == false) {
					str.deleteCharAt(i);
					i = i - 1;
				}
				i = i + 1;
			}
			
			if (str.length() == 1) {
				return false;
			}
			
			String s3 = str.toString();
			StringBuilder str2 = str.reverse();
		
			String s4 = str2.toString();
			
			if (s3.equalsIgnoreCase(s4)) {
				return true;
			}
			else {
				return false;
				}
				
			}

		}
	

