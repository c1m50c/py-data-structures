from binary_tree import BinaryTree, Node


def test_node_insertion():
    node = Node(value=1, left=None, right=None)
    node.insert(value=2)
    node.insert(value=3)
    assert node.value == 1
    assert node.right.value == 2
    assert node.right.right.value == 3


def test_tree_from_list():
    tree = BinaryTree(from_list=[1, 2, 3])
    assert tree.root.value == 1
    assert tree.root.right.value == 2
    assert tree.root.right.right.value == 3


def test_tree_insertion():
    tree = BinaryTree()
    tree.insert(value=1)
    tree.insert(value=2)
    tree.insert(value=3)
    assert tree.root.value == 1
    assert tree.root.right.value == 2
    assert tree.root.right.right.value == 3


def test_clear():
    tree = BinaryTree()
    tree.insert(value=1)
    tree.insert(value=2)
    tree.insert(value=3)
    tree.clear()
    assert tree.root == None


def test_node_remove():
    node = Node(value=1, left=None, right=None)
    node.insert(value=2)
    node.insert(value=3)
    node.insert(value=4)
    node.insert(value=5)
    node.remove(value=3, root=node)
    assert node.value == 1
    assert node.right.value == 2
    assert node.right.right.value == 4


def test_tree_remove():
    tree = BinaryTree(from_list=[1, 2, 3, 4, 5])
    tree.remove(value=3)
    assert tree.root.value == 1
    assert tree.root.right.value == 2
    assert tree.root.right.right.value == 4


if __name__ == "__main__":
    test_node_insertion()
    test_tree_from_list()
    test_tree_insertion()
    test_clear()
    test_node_remove()
    test_tree_remove()