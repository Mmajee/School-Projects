package cp213;

/**
 * The individual node of a doubly-linked structure that stores Movie
 * objects. This is a doubly-linked node. The node link can be updated,
 * but not the node data, in order to avoid moving data between nodes.
 * Data structures must be reordered by moving nodes.
 *
 * @author 
 * @version 2019-10-08
 */
public final class DoubleNode {

    // Link to the next DoubleNode.
    private DoubleNode next = null;
    // Link to the previous DoubleNode.
    private DoubleNode prev = null;
    // The Movie data.
    private Movie value = null;

    /**
     * Creates a new node with data and link to the previous and next nodes. Not
     * copy safe as it accepts a reference to the data rather than a copy of the
     * data.
     *
     * @param value
     *            the data to store in the node.
     * @param next
     *            the previous node to link to.
     * @param next
     *            the next node to link to.
     */
    public DoubleNode(final Movie value, final DoubleNode prev,
	    final DoubleNode next) {
    	
    	this.value = value;
    	setPrev(prev);
    	setNext(next);
    }

    /**
     * Returns the next node in the linked structure.
     *
     * @return The node that follows this node. Must be copy safe.
     */
    public final DoubleNode getNext() {
    	DoubleNode newNext;
    	
    	newNext = this.next;
    	
    	return newNext;
    }

    /**
     * Returns the previous node in the linked structure.
     *
     * @return The node that precedes this node. Must be copy safe.
     */
    public final DoubleNode getPrev() {
    	DoubleNode newPrev;
    	
    	newPrev = this.prev;
    	
    	return newPrev;
    }

    /**
     * Returns the node data. Must be copy safe.
     *
     * @return The data portion of the node.
     */
    public final Movie getValue() {
    	
    	Movie newValue;
    	
    	newValue = this.value;
    	
    	return newValue; 
    }

    /**
     * Links this node to the next node.
     *
     * @param next
     *            The new node to link to.
     */
    public final void setNext(final DoubleNode next) {
    	this.next = next;
    }

    /**
     * Links this node to the previous node.
     *
     * @param prev
     *            The new node to link to.
     */
    public final void setPrev(final DoubleNode prev) {
    	this.prev = prev;
    }
}
