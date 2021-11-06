from binary_tree import BinaryTree, Node


def test_node_insertion():
    node = Node(value=1, left=None, right=None)
    node.insert(value=2)
    node.insert(value=3)
    assert node.value == 1
    assert node.right.value == 2
    assert node.right.right.value == 3


def test_tree_insertion():
    tree = BinaryTree()
    tree.insert(value=1)
    tree.insert(value=2)
    tree.insert(value=3)
    assert tree.root.value == 1
    assert tree.root.right.value == 2
    assert tree.root.right.right.value == 3


if __name__ == "__main__":
    test_node_insertion()
    test_tree_insertion()