package cp213;


import java.util.Scanner;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

/**
 * Process text files with three kinds of trees to determine their relative
 * efficiency.
 *
 * @author your name here
 * @version 2018-07-05
 */
public class A04 {
	
    /**
     * Program for Assignment 4.
     *
     * @param args
     *            unused
     * @throws IOException
     *             If error on files.
     */
    public static void main(final String[] args) throws IOException {
    	BST tree = new BST();
    	PopularityTree tree2 = new PopularityTree();
    	
    	
    	File file = new File("src/decline.txt");
    	File file2 = new File("src/miserables.txt");
    	File file3 = new File("src/otoos610.txt");
    	
    	
    	System.out.println("Training File: " + file.getName());
    	System.out.println("Comparisons File: " + file2.getName());
    	System.out.println("--------------------------");
    	train(tree, file);
    	
    	System.out.println("Character Table for Training File");
    	System.out.println();
    	characterTable(tree);
    	System.out.println("--------------------------");
    	
    	System.out.println("Tree Type: BST");
    	System.out.println("Training...");
    	System.out.println("Valid: " + tree.isValid());
    	System.out.println("Height: " + tree.root.getHeight());	
    	System.out.println("Retrieving...");
    	int compare = retrieve(tree, file2);
    	System.out.printf("%,d Comparisons: " , compare);
    	System.out.print("\n");
    	System.out.println("------------------------");
    	train(tree2, file);
    	
    	System.out.println("Tree Type: Popularity Tree");
    	System.out.println("Training...");
    	System.out.println("Valid: " + tree2.isValid());
    	System.out.println("Height: " + tree2.root.getHeight());
    	System.out.println("Retrieving...");
    	int compare2 = retrieve(tree2, file2);
    	System.out.printf("%,d Comparisons: " , compare2);
    	System.out.print("\n");
    	System.out.println("------------------------");
    	
    	if (compare < compare2) {
    		System.out.println("Tree with minimum comparisons: BST");
    	}
    	else {
    		System.out.println("Tree with minimum comparisons: Popularity Tree");
    	}

    }

    /**
     * Determine the number of comparisons to retrieve the contents of a file
     * from a tree. Reset the number of comparisons, then attempt to retrieve
     * every letter in the file from tree. All letters must be converted to
     * upper case.
     *
     * @param tree
     *            The BST to process.
     * @param file
     *            The file to process.
     * @return The number of comparisons necessary to find every letter in file
     *         in tree.
     * @throws FileNotFoundException
     *             Thrown if file not found.
     */
    public static int retrieve(final BST<Character> tree, final File file)
	    throws FileNotFoundException {
    	tree.resetComparisons(); 	 
    	
    	Scanner readFile = new Scanner(new FileInputStream(file));
    	
    	String input;
		
    	while (readFile.hasNextLine()) {
    		input = readFile.nextLine();
    		for (int i = 0; i < input.length(); i++) {
    			char letter = input.charAt(i);
    			if (Character.isLetter(letter)) {
    				tree.retrieve(Character.toUpperCase(letter));
    			}
    			
    		}
    	}
    	
    	readFile.close();
    	
    	return tree.getComparisons();
    }

    /**
     * Train a tree by inserting all letters from a file into the tree. Letters
     * must be converted to upper-case. Non-letters are ignored.
     *
     * @param tree
     *            The BST to train.
     * @param file
     *            The file to read into the tree.
     * @throws FileNotFoundException
     *             Thrown if file not found.
     */
    public static void train(final BST<Character> tree, final File file)
	    throws FileNotFoundException {
    	
    	Scanner readFile = new Scanner(new FileInputStream(file));
    	
    	String input; 
	
    	while(readFile.hasNextLine()) {
    		input = readFile.nextLine();
    		for (int i = 0; i < input.length(); i++) {
    			char letter = input.charAt(i);
    			if (Character.isLetter(letter)) {
    				tree.insert(Character.toUpperCase(letter));
    			}
    			
    		}
    	}
    	
    	readFile.close();
    }
    
    public static void characterTable(final BST<Character> tree) {
    	System.out.print("Char");
    	System.out.printf("%8s", "Count");
    	System.out.printf("%9s", "Percent");
    	System.out.print("\n");
    	
    	TreeNode[] array = tree.toArray();
    	
    	int totalCount = 0;
    	
    	for (TreeNode value: array) {
    		totalCount += value.getCount();
    	}
    	
    	double percent = 0;
    	for(TreeNode value: array) {
    		
    		percent = ((double)value.getCount() / totalCount) * 100;
    		System.out.printf("%4s", value.getData().toString());
    		System.out.printf("%,8d", value.getCount());
    		System.out.printf("%9.2f", percent);
    		System.out.print("\n");
    	}
    }
}
