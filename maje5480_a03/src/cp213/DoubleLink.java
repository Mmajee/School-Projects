package cp213;

/**
 * The class for doubly-linked data structures. Provides attributes
 * and implementations for getLength, isEmpty, and toArray methods.
 * The head attribute is the first node in any doubly-linked list and
 * last is the last node.
 *
 * @author 
 * @version 2019-10-08
 * 
 */
public class DoubleLink {

    // First node of double linked list
    private DoubleNode head = null;

    // Number of elements currently stored in linked list
    private int length = 0;

    // Last node of double linked list.
    private DoubleNode last = null;

    /**
     * Adds a new Movie element to the list at the head position
     * before the previous head, if any. Increments the length of the List.
	 *
     * @param value
     *            The value to be added at the head of the list.
	 *
     * @return true if node is added successfully, else false.
     */
    public final boolean addNode(final Movie value) {
    	
    	DoubleNode node = new DoubleNode(value, null, this.head);
    	
    	if (this.length == 0) {	
    		this.head = node;
    		this.last = node;
    	}
    	else {
    		DoubleNode temp;
    		
    		temp = this.head;
    		this.head = node;
    		temp.setPrev(head);
    		head.setNext(temp);
    	}
    	
    	length += 1;
    	
    	return true;
    }

    /**
     * Removes the value at the front of this List.
     *
     * @return The value at the front of this List.
     */
    public Movie removeFront() {
    	Movie value = null;
    	DoubleNode temp;
    	
    	
    	if (head != null) {
    		value = head.getValue();
        	temp = head;
        	head = head.getNext();
        	
        	if (head != null) {
        		head.setPrev(null);
            	temp.setNext(null);
        	}	
    	}
    	length -= 1;
    	
    	
    	return value;
    }
    
    /**
     * Returns the head element in the linked structure. Must be copy safe.
     *
     * @return the head node.
     */
    public final DoubleNode getHead() {
    	DoubleNode front;
    	
    	front = this.head;
    	
    	return front;
    }

    /**
     * Returns the current number of elements in the linked structure.
     *
     * @return the value of length.
     */
    public final int getLength() {	
    	return length;
    }

    /**
     * Returns the last node in the linked structure. Must be copy safe.
     *
     * @return the last node.
     */
    public final DoubleNode getLast() {
    	DoubleNode rear;
    	
    	rear = this.last;
    	return rear;
    }

    /**
     * Determines whether the double linked list is empty or not.
     *
     * @return true if list is empty, false otherwise.
     */
    public final boolean isEmpty() {

    	return length == 0;
    }

    /**
     * Returns all the data in the list in the form of an array.
     *
     * @return The array of Movie elements. Must be copy safe
     */
    public final Movie [] toArray() {

    	Movie[] movieArray = new Movie[length];	
    	DoubleNode current;
    	
    	int count = 0;
    	current = this.head;
    	
    	while (!current.equals(null) & count <= length)  {
    		
    		movieArray[count] = current.getValue();
    		current = current.getNext();
    		
    	}
    	
    	return movieArray;
    }
    

}
