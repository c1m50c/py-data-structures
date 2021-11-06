from linked_list import LinkedList


def test_from_list():
    linked_list = LinkedList(from_list=[1, 2, 3])
    assert len(linked_list) == 3
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 3


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


if __name__ == "__main__":
    test_from_list()
    test_clear()
    test_push_front()
    test_push_back()
    test_append()