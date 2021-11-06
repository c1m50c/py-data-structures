from linked_list import LinkedList


def test_push_front():
    linked_list: LinkedList = LinkedList()
    linked_list.push_front(1)
    linked_list.push_front(2)
    linked_list.push_front(3)
    assert len(linked_list) == 3
    assert linked_list.head.value == 3 and linked_list.tail.value == 1


def test_push_back():
    linked_list: LinkedList = LinkedList()
    linked_list.push_back(1)
    linked_list.push_back(2)
    linked_list.push_back(3)
    assert len(linked_list) == 3
    assert linked_list.head.value == 1 and linked_list.tail.value == 3


test_push_front()
test_push_back()