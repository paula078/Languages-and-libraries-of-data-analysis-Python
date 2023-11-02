# Task 1 Binary Search Tree

class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_node(self, data):
        # If that node already exists (we don't need to do anything)
        if data == self.data:
            return

        if data < self.data:
            # add data in left subtree
            if self.left:
                # If the left element has some value (we need to go to its child node)
                self.left.add_node(data)
            else:
                # If left node is None (empty)
                self.left = BinarySearchTree(data)
        else:
            # add data in right subtree
            if self.right:
                # If the right element has some value (we need to go to its child node)
                self.right.add_node(data)
            else:
                # If right node is None (empty)
                self.right = BinarySearchTree(data)

    def search(self, node):
        if self.data == node:
            return True

        if node < self.data:
            if self.left:
                return self.left.search(node)
            else:
                return False

        if node > self.data:
            if self.right:
                return self.right.search(node)
            else:
                return False


def build_tree(elements):
    tree_root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        tree_root.add_node(elements[i])

    return tree_root


def in_order(self, tree_nodes):
    if self is not None:
        # visit left tree
        in_order(self.left, tree_nodes)

        # visit root node
        tree_nodes.append(str(self.data))

        # visit right tree
        in_order(self.right, tree_nodes)


if __name__ == '__main__':
    print("Method 1")
    tree_1 = BinarySearchTree(55)
    tree_1.add_node(50)
    tree_1.add_node(98)
    tree_1.add_node(10)
    tree_1.add_node(78)
    tree_1.add_node(66)

    tree_in_order = []
    in_order(tree_1, tree_in_order)
    print("In-order traversal:", " -> ".join(tree_in_order))

    print("Does the number 10 belong to a tree? ", tree_1.search(14))


    print("\nMethod 2 (more convenient)")
    tree_2 = build_tree([8, 13, 3, 1, 14, 6, 4, 7, 8, 10])

    tree_in_order = []
    in_order(tree_2, tree_in_order)
    print("In-order traversal:", " -> ".join(tree_in_order))

    print("Does the number 10 belong to a tree? ", tree_2.search(14))
