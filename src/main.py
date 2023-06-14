from binary_tree import buildTree


def main():
    elements = [12, 1, 50, 32, 5, 10, 9, 2, 38, 25, 22, 45, 8]
    tree = buildTree(elements)
    # 1- Build In-Order Binary Search Tree
    print(tree.in_order_traversal())  # It returns a sorted array
    print(tree.searchTree(20))  # False
    print(tree.searchTree(50))  # True

    # 2- Build Pre-Order Binary Search Tree
    print(tree.pre_order_traversal())
    # 3- Build Post-Order Binary Search Tree
    print(tree.post_order_traversal())


if __name__ == "__main__":
    main()
