package cp213;

/**
 * The individual node of a linked structure that stores {@code T} objects and a
 * count. This is a doubly-linked node with left and right pointers to child
 * nodes. The node link can be updated, but not the node data, in order to avoid
 * moving data between nodes. Data structures must be reordered by moving nodes.
 *
 * @author David Brown
 * @version 2018-07-09
 */
public class TreeNode<T extends Comparable<T>> {

    // The T data and count.
    private T data = null;
    private int count = 1;
    // Link to the child TreeNodes.
    private TreeNode<T> left = null;
    private TreeNode<T> right = null;
    private int height = 1;

    /**
     * Creates a new TreeNode with data and null links to its child TreeNodes.
     * Not copy safe as it accepts a reference to the data rather than a copy of
     * the data.
     *
     * @param data
     *            The data to store in the node.
     */
    public TreeNode(final T data) {
	this.data = data;
    }

    /**
     * Decrements the data count of this TreeNode by 1.
     */
    public void decrementCount() {
	this.count--;
    }

    /**
     * Returns the data count of this TreeNode.
     *
     * @return count.
     */
    public int getCount() {
	return this.count;
    }

    /**
     * Returns this TreeNode data. Not copy safe as it returns a reference to
     * the data, not a copy of the data.
     *
     * @return The data portion of this TreeNode.
     */
    public T getData() {
	return this.data;
    }

    /**
     * Returns the height of this TreeNode.
     *
     * @return height.
     */
    public int getHeight() {
	return this.height;
    }

    /**
     * Returns the left child of this TreeNode.
     *
     * @return left.
     */
    public TreeNode<T> getLeft() {
	return this.left;
    }

    /**
     * Returns the right child of this TreeNode.
     *
     * @return right.
     */
    public TreeNode<T> getRight() {
	return this.right;
    }

    /**
     * Increments the data count of this TreeNode by 1.
     */
    public void incrementCount() {
	this.count++;
    }

    /**
     * Updates the left child reference of this TreeNode to another TreeNode.
     *
     * @param left
     *            The new TreeNode to link to.
     */
    public void setLeft(final TreeNode<T> left) {
	this.left = left;
    }

    /**
     * Updates the right child reference of this TreeNode to another TreeNode.
     *
     * @param right
     *            The new TreeNode to link to.
     */
    public void setRight(final TreeNode<T> right) {
	this.right = right;
    }

    @Override
    public String toString() {
	return "V: " + this.data + "; C: " + this.count + "; H: " + this.height;
    }

    /**
     * Updates the height of this TreeNode to 1 plus the maximum heights of its
     * two child nodes. Empty child nodes have a height of 0.
     */
    public void updateHeight() {
	int leftHeight = 0;
	int rightHeight = 0;

	if (this.left != null) {
	    leftHeight = this.left.height;
	}
	if (this.right != null) {
	    rightHeight = this.right.height;
	}
	this.height = Math.max(leftHeight, rightHeight) + 1;
	return;
    }

}
