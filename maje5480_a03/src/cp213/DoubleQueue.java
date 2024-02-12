package cp213;

/**
 * A queue structure of Movie objects. Only the Movie values contained
 * in the queue are visible through the standard queue methods. The Movie
 * values are stored in a DoubleLink object provided in class as attribute.
 *
 * @author 
 *
 * @version 2019-10-08
 *
 * @param Movie
 *            this data structure value type.
 */
public class DoubleQueue {

    // First node of the queue
    private DoubleLink values = null;

    /**
     * Combines the contents of the left and right Queues into the current
     * Queue. Moves nodes only - does not move value or call the high-level
     * methods insert or remove. left and right Queues are empty when done.
     * Nodes are moved alternately from left and right to this Queue.
     *
     * @param source1
     *            The front Queue to extract nodes from.
     * @param source2
     *            The second Queue to extract nodes from.
     */
    public void combine(final DoubleQueue source1,
	    final DoubleQueue source2) {
    	
    	DoubleLink tempNode = new DoubleLink();
    	DoubleLink current;
    	DoubleLink current2;
    	DoubleLink tempValues = new DoubleLink();
    	Movie value;
    	
    	values = tempNode;
    	boolean left = true;
    	current = source1.values;
    	current2 = source2.values;
    	
    	while ((current.getLength() != 0) || (current2.getLength() != 0)) {
    		
    		if ((left == true) && (current.getLength() != 0)) {
    			value = current.removeFront();
    			values.addNode(value);
    			left = false;
    		}
    		else if ((left == false) && (current2.getLength() != 0)) {
    			value = current2.removeFront();
    			values.addNode(value);
    			left = true;
    		}
    	
    	}
    	
    	while (values.getLength() != 0) {
    		value = values.removeFront();
    		tempValues.addNode(value);
    	}
    	values = tempValues;
    }

    /**
     * Adds value to the rear of the queue.
     *
     * @param value
     *            The value to added to the rear of the queue.
     */
    public void insert(final Movie value) {
    		
    	DoubleNode temp;
    	
    	if (values == null) {
    		   		
    		DoubleLink thisValues = new DoubleLink();
    		
    		values = thisValues;
    		
    		values.addNode(value);
    	}
    	else {
    		//temp = values.getHead();
    		//DoubleNode node = new DoubleNode(value, null, temp);
    		//temp.setPrev(node);
    		values.addNode(value);
    		
    	}    	
    	   
    }

    /**
     * Returns the front value of the queue and removes that value from the
     * queue. The next node in the queue becomes the new front node.
     *
     * @return The value at the front of the queue.
     */
    public Movie remove() {
    	
    	Movie value = null;
    	Movie tempValue;
    	
    	DoubleLink newValues = new DoubleLink();
    	
    	
    	while (values.getLength() != 0) {
    		tempValue = values.removeFront();
    		newValues.addNode(tempValue);
    	}
    	
    	value = newValues.removeFront();
    	
    	
    	while (newValues.getLength() != 0) {
    		tempValue = newValues.removeFront();
    		values.addNode(tempValue);
    	}
    	
    	return value;
    }

    /**
     * Returns the value at the front. Must be copy safe
     *
     * @return the value at the front.
     */
    public Movie peekFront() {
    	DoubleNode front;
    	
    	front = this.values.getLast();
    	return front.getValue();
    }

    /**
     * Returns the value at the rear. Must be copy safe.
     *
     * @return the value at the rear.
     */
    public Movie peekRear() {
    	DoubleNode rear;
    	
    	rear = this.values.getHead();
    	return rear.getValue();
    }

    /**
     * Returns all the data in the queue in the form of an array.
     *
     * @return The array of Movie elements. Must be copy safe
     */
    public final Movie [] toArray() {
    	Movie[] movieArray = new Movie[this.values.getLength()];
    	DoubleNode current;
    	Movie value;
    	
    	current = this.values.getHead();
    	
    	for (int i = this.values.getLength() - 1; i >= 0; i --) {
    		
    		value = current.getValue();
    		movieArray[i] = value;
    		current = current.getNext();
    		
    	}
    	return movieArray;
    }

}
