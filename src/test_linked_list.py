from linked_list import LinkedList


def test_from_list():
    linked_list = LinkedList(from_list=[1, 2, 3])
    assert len(linked_list) == 3
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 3


def test_str():
    linked_list = LinkedList(from_list=[4, 0, 4])
    assert str(linked_list) == "[4, 0, 4]"
    linked_list.clear()
    assert str(linked_list) == "[]"


def test_eq_ne():
    linked_list_one = LinkedList(from_list=[6, 6, 6])
    linked_list_two = LinkedList(from_list=[6, 6, 6])
    assert linked_list_one == linked_list_two
    linked_list_two.remove_back()
    assert linked_list_one != linked_list_two


def test_clear():
    linked_list = LinkedList(from_list=[1, 2, 3])
    linked_list.clear()
    assert len(linked_list) == 0
    assert linked_list.head == None
    assert linked_list.tail == None


def test_push_front():
    linked_list = LinkedList()
    linked_list.push_front(1)
    linked_list.push_front(2)
    linked_list.push_front(3)
    assert len(linked_list) == 3
    assert linked_list.head.value == 3
    assert linked_list.tail.value == 1


def test_push_back():
    linked_list = LinkedList()
    linked_list.push_back(1)
    linked_list.push_back(2)
    linked_list.push_back(3)
    assert len(linked_list) == 3
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 3


def test_append():
    linked_list_one = LinkedList(from_list=[1, 2, 3])
    linked_list_two = LinkedList(from_list=[4, 5, 6])

    linked_list_one.append(other=linked_list_two)
    
    assert len(linked_list_one) == 6
    assert linked_list_one.head.value == 1
    assert linked_list_one.tail.value == 6
    assert len(linked_list_two) == 0


def test_remove_front():
    linked_list = LinkedList(from_list=[1, 3, 3, 7])
    linked_list.remove_front()
    assert len(linked_list) == 3
    assert linked_list.head.value == 3
    
    linked_list.clear()
    linked_list.remove_back()
    assert len(linked_list) == 0
    assert linked_list.tail == None


def test_remove_back():
    linked_list = LinkedList(from_list=[1, 3, 3, 7])
    linked_list.remove_back()
    assert len(linked_list) == 3
    assert linked_list.tail.value == 3
    
    linked_list.clear()
    linked_list.remove_back()
    assert len(linked_list) == 0
    assert linked_list.tail == None


def test_get():
    linked_list = LinkedList(from_list=[7, 8, 7])
    assert linked_list.get(1) == 8


def test_search():
    linked_list = LinkedList(from_list=[1, 2, 3, 4, 5])
    idx: int = linked_list.search(3)
    assert idx == 2


if __name__ == "__main__":
    test_from_list()
    test_str()
    test_eq_ne()
    test_clear()
    test_push_front()
    test_push_back()
    test_append()
    test_remove_front()
    test_remove_back()
    test_get()
    test_search()