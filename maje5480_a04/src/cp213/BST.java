package cp213;

import java.util.ArrayList;

/**
 * Implements a Binary Search Tree.
 *
 * - author your name here -
 *
 * @version 2018-07-12
 *
 * @param <T> The data to store in the tree.
 */
public class BST<T extends Comparable<T>> {

    private int comparisons = 0;
    // Attributes.
    protected TreeNode<T> root = null;
    protected int size = 0;

    /**
     * Determines if this BST contains key.
     *
     * @param key The key to search for.
     * @return true if this BST contains key, false otherwise.
     */
    public boolean contains(final T key) {
		
    	TreeNode<T> node = root;
    	T value = node.getData();
    	
    	while ((node != null) && (key != value)) {
    		
    		if (key.compareTo(value) < 0) {
    			node = node.getLeft();
    			
    			if (node != null) {
    				value = node.getData();
    			}
    		}
    		else {
    			node = node.getRight();
    			if (node != null) {
    				value = node.getData();
    			}
    		}
    	}
    	
    	if (node != null) {
    		return true;
    	}
    	else {
    		return false;
    	}
    		

    }

    /**
     * Determines whether two BSTs are identical.
     *
     * @param that The BST to compare this BST against.
     * @return true if this BST and that BST contain nodes that match in
     *         position, value, count, and height, false otherwise.
     */

    public boolean equals(final BST<T> that) {

		if (this.size != that.size) {
			return false;
		}
		else {
			boolean same = false;
			
			return equals_aux(this.root, that.root, same);
		}

    }
    

    /**
     * Get number of comparisons executed by the {@code retrieve} method.
     *
     * @return comparisons
     */
    public int getComparisons() {
    	return this.comparisons;
    }

    /**
     * Returns the height of the root node of this BST.
     *
     * @return height of root node, 0 if the root node is null.
     */
    public int getHeight() {

		return root.getHeight();

    }

    /**
     * Returns the number of nodes in the BST.
     *
     * @return size of this BST.
     */
    public int getSize() {

		return size;

    }

    /**
     * Inserts data into this BST.
     *
     * @param data Data to store.
     */
    public void insert(final T data) {

		TreeNode<T> node;
		TreeNode<T> previous = null;
		
		node = this.root;
		while ((node != null) && (data.compareTo(node.getData()) != 0)) {
			if (data.compareTo(node.getData()) < 0 ) {
				previous = node;
				node = node.getLeft();
			}
			else {
				previous = node;
				node = node.getRight();
			}
		}

		if ((node == null) && (previous == null)) {
			
			TreeNode<T> newNode = new TreeNode<T>(data);
			this.root = newNode;
			size += 1;
		}
		else if(node == null){
			
			TreeNode<T> newNode = new TreeNode<T>(data);
			if (data.compareTo(previous.getData()) < 0) {
				previous.setLeft(newNode);
			}
			else {
				previous.setRight(newNode);
				}
			size += 1;
			}
		else{
			node.incrementCount();
		}
		set_all_height(root);
			
		}


    /**
     * Determines if this BST is empty.
     *
     * @return true if this BST is empty, false otherwise.
     */
    public boolean isEmpty() {

		return size == 0;

    }

    /**
     * Determines if this BST is a valid BST; i.e. a node's left child data is
     * smaller than its data, and its right child data is greater than its data.
     * The height of a node is equal to the maximum of the heights of its two
     * children (missing child nodes have a height of 0), plus 1.
     *
     * @return true if this BST is a valid BST, false otherwise.
     */ 
    public boolean isValid() {
    	
    	return isValid_aux(root, root.getLeft(), root.getRight());
    	
    }
    


    /**
     * Resets the comparison count to 0.
     */
    public void resetComparisons() {
		this.comparisons = 0;
		return;
    }

    /**
     * Retrieves the node whose data matches key. Returning a TreeNode gives
     * access to the node data and count.
     *
     * @param key The key to look for.
     * @return A DataCountPair object that contains the data that matches key
     *         and its count, null otherwise.
     */
    public TreeNode<T> retrieve(final T key) {
    	
    	TreeNode<T> node = root;
    	comparisons += 1;
    	
    	while ((node != null) && (key != node.getData())) {
    		
    		
    		if (key.compareTo(node.getData()) < 0 ) {
				node = node.getLeft();
			}
			else {
				node = node.getRight();
			}
    		comparisons += 1;
		}
    	
    	return node;
    }

    /**
     * Returns an array of tree nodes from a linked data structure. Not thread
     * safe as it assumes contents of data structure are not changed by an
     * external thread during the copy loop. If data elements are added or
     * removed by an external thread while the data is being copied to the
     * array, then the declared array size may no longer be valid. The array
     * contents are in data order.
     *
     * @return the tree nodes of a bst as an array of nodes.
     */
    @SuppressWarnings("unchecked")
    public final TreeNode<T>[] toArray() {
		final ArrayList<TreeNode<T>> queue = new ArrayList<>();
		this.toArrayAux(this.root, queue);
		return queue.toArray(new TreeNode[queue.size()]);
    }

    /**
     * Performs an inorder traversal of a tree copying nodes to a queue.
     *
     * @param node  a TreeNode
     * @param queue temporary structure to hold nodes
     */
    private final void toArrayAux(final TreeNode<T> node,
	    final ArrayList<TreeNode<T>> queue) {
		if (node != null) {
		    this.toArrayAux(node.getLeft(), queue);
		    queue.add(node);
		    this.toArrayAux(node.getRight(), queue);
	}
    }

    /**
     * Returns the height of a given TreeNode.
     *
     * @param node The TreeNode to determine the height of.
     * @return The value of the height attribute of node, 0 if node is null.
     */
    protected int nodeHeight(final TreeNode<T> node) {

		
    	if (node == null) {
			return 0;
		}
		else {
			int heightLeft;
			int heightRight;
			
			if (node.getLeft() == null) {
				heightLeft = 0;
			}
			else {
				heightLeft = node.getLeft().getHeight();
			}
			
			if (node.getRight() == null) {
				heightRight = 0;
			}
			else {
				heightRight = node.getRight().getHeight();
			}
			
			return Math.max(heightLeft, heightRight) + 1;
		}

    }
    
    private boolean equals_aux(TreeNode<T> node1,TreeNode<T> node2, boolean same) {
		
    	if ((node1 == null) && (node2 == null)) {
    		return same;
    	}
    	else if ((node1 == null) && (node2 != null)) {
    		same = false;
    	}
    	else if ((node1 != null) && (node2 == null)) {
    		same = false;
    	}
    	else if (node1.getData() != node2.getData()) {
    		same = false;
    	}
    	else if (node1.getData() == node2.getData()) {
    		same = true;
    	
	    	same = equals_aux(node1.getLeft(), node2.getLeft(), same);
	    	
	    	same = equals_aux(node1.getRight(), node2.getRight(), same);
	    	
    	}
		return same;
    }
    
    private void set_all_height(TreeNode<T> node) {
    	
    	if (node == null) {
    		return;
    	}
    	else {
    		set_all_height(node.getLeft());
    		node.updateHeight();
    		set_all_height(node.getRight());
    		node.updateHeight();
    	}
    }
    
    private boolean isValid_aux(TreeNode<T> root, TreeNode<T> left, TreeNode<T> right) {
    	
    	if (root == null) {
    		return true;
    	}
    	else if (left == null) {
    		return true;
    	}
    	else if (right == null) {
    		return true;
    	}
    	else if(root.getData().compareTo(left.getData()) < 0) {
    		return false;
    	}
    	else if(root.getData().compareTo(right.getData()) > 0) {
    		return false;
    	}
    	else if(this.nodeHeight(root) != Math.max(this.nodeHeight(left), this.nodeHeight(right)) + 1)
    		return false;
    	else {
    		isValid_aux(root.getLeft(), root.getLeft().getLeft(), root.getLeft().getRight());
    		
    		isValid_aux(root.getRight(), root.getRight().getLeft(), root.getRight().getRight());
    	}
    	return true;
    }

}
