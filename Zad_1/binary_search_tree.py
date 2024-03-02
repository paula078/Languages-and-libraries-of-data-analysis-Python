# Task 1 Binary Search Tree

class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_vertex(self, data):
        # If that vertex already exists (we don't need to do anything)
        if data == self.data:
            return

        if data < self.data:
            # add data in left subtree
            if self.left:
                # If the left element has some value (we need to go to its child vertex)
                self.left.add_vertex(data)
            else:
                # If left vertex is None (empty)
                self.left = BinarySearchTree(data)
        else:
            # add data in right subtree
            if self.right:
                # If the right element has some value (we need to go to its child vertex)
                self.right.add_vertex(data)
            else:
                # If right vertex is None (empty)
                self.right = BinarySearchTree(data)

    def search(self, vertex):
        if self.data == vertex:
            return True

        if vertex < self.data:
            if self.left:
                return self.left.search(vertex)
            else:
                return False

        if vertex > self.data:
            if self.right:
                return self.right.search(vertex)
            else:
                return False

    def in_order(self, tree_vertices):
        if self is not None:
            # Sprawdź lewe poddrzewo
            if self.left:
                self.left.in_order(tree_vertices)

            # Dodaj bieżący węzeł do listy
            tree_vertices.append(self.data)

            # Sprawdź prawe poddrzewo
            if self.right:
                self.right.in_order(tree_vertices)


def build_tree(elements):
    tree_root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        tree_root.add_vertex(elements[i])

    return tree_root

if __name__ == '__main__':
    print("Method 1")
    tree_1 = BinarySearchTree(55)
    tree_1.add_vertex(50)
    tree_1.add_vertex(98)
    tree_1.add_vertex(10)
    tree_1.add_vertex(78)
    tree_1.add_vertex(66)

    tree_in_order = []
    tree_1.in_order(tree_in_order)
    print("In-order traversal:", " -> ".join(str(vertex) for vertex in tree_in_order))
    vertex_to_check = 14
    print(f"Does the number {vertex_to_check} belong to a tree? ", tree_1.search(vertex_to_check))


    print("\nMethod 2 (more convenient)")
    tree_2 = build_tree([8, 13, 3, 1, 14, 6, 4, 7, 8, 10])

    tree_in_order = []
    tree_2.in_order(tree_in_order)
    print("In-order traversal:", " -> ".join(str(vertex) for vertex in tree_in_order))

    print(f"Does the number {vertex_to_check} belong to a tree? ", tree_2.search(vertex_to_check))
