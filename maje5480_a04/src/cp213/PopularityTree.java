package cp213;

/**
 * Implements a Popularity Tree. Extends BST.
 *
 * @author your name here
 * @version 2018-07-05
 *
 * @param <T>
 *            The data to store in the tree.
 */
public class PopularityTree<T extends Comparable<T>> extends BST<T> {

	public void insert(T data) {
		
		super.insert(data);
	
		this.do_rotation(root, null, null);
		
	}
	
	private void do_rotation(TreeNode<T> current, TreeNode<T> previous, TreeNode<T> previous2) {
	
		
		if (current == null) {
			return;
		}
		else if ((current.getLeft() != null) && (current.getCount() < current.getLeft().getCount())) {
			TreeNode<T> temp = current.getLeft();
			current.setLeft(null);
			TreeNode<T> temp2 = temp.getRight();
			
			temp.setRight(current);
			current.setLeft(temp2);
			current.updateHeight();
			
			if (current.equals(root)) {
				root = temp;
				previous = null;
				root.updateHeight();
			}
			
			if (previous != null) {
				if (previous.getRight() == current) {
					previous.setRight(temp);
				}
				else {
					 previous.setLeft(temp);
				}
				
			current = temp;
			current.updateHeight();
			if (previous != null) {
				previous.updateHeight();
			}
			if ((previous != null) && (previous.getRight() != null) && (previous.getCount() < previous.getRight().getCount())) {
				do_rotation(previous, previous2, null);
					}
				}
			}
		else if((current.getRight() != null) && (current.getCount() < current.getRight().getCount())) {
			TreeNode<T> temp = current.getRight();
			current.setRight(null);
			TreeNode<T> temp2 = temp.getLeft();
			
			temp.setLeft(current);
			current.setRight(temp2);
			current.updateHeight();
			
			if (current.equals(root)) {
				root = temp;
				previous = null;
				root.updateHeight();
			}
			
			if (previous != null) {
				if (previous.getRight() == current) {
					previous.setRight(temp);
				}
				else {
					 previous.setLeft(temp);
				}
			}
			
		current = temp;
		current.updateHeight();
		if (previous != null) {
			previous.updateHeight();
			}
		if ((previous != null) &&  (previous.getLeft() != null) && (previous.getCount() < previous.getLeft().getCount())) {
			do_rotation(previous, previous2, null);
			}
		}
		else{
			do_rotation(current.getLeft(), current, previous);
			do_rotation(current.getRight(), current, previous);
		}
		
		
	}

}
