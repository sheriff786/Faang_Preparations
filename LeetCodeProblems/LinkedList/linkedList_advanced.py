from collections import defaultdict, OrderedDict


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None
        self.child = None


class RandomNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def values(self):
        result = []
        current_node = self.head
        while current_node is not None:
            result.append(current_node.data)
            current_node = current_node.next
        return result

    def reverse_recursive(self):
        self.head = self._reverse_recursive(self.head)

    def _reverse_recursive(self, current_node):
        if current_node is None or current_node.next is None:
            return current_node

        new_head = self._reverse_recursive(current_node.next)
        current_node.next.next = current_node
        current_node.next = None
        return new_head

    def remove_duplicates_sorted(self):
        current_node = self.head
        while current_node is not None and current_node.next is not None:
            if current_node.data == current_node.next.data:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next

    def remove_duplicates_unsorted(self):
        seen_values = set()
        previous_node = None
        current_node = self.head

        while current_node is not None:
            if current_node.data in seen_values:
                previous_node.next = current_node.next
            else:
                seen_values.add(current_node.data)
                previous_node = current_node
            current_node = current_node.next

    def reverse_sublist(self, left, right):
        if left < 1 or right < left:
            raise ValueError("left and right must be valid positions")
        if self.head is None or left == right:
            return

        dummy_node = Node(0)
        dummy_node.next = self.head
        before_sublist = dummy_node

        for _ in range(left - 1):
            if before_sublist.next is None:
                raise ValueError("position is outside the list")
            before_sublist = before_sublist.next

        sublist_tail = before_sublist.next
        if sublist_tail is None:
            raise ValueError("position is outside the list")

        current_node = sublist_tail.next
        for _ in range(right - left):
            if current_node is None:
                raise ValueError("position is outside the list")
            sublist_tail.next = current_node.next
            current_node.next = before_sublist.next
            before_sublist.next = current_node
            current_node = sublist_tail.next

        self.head = dummy_node.next

    def swap_pairs(self):
        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node

        while previous_node.next is not None and previous_node.next.next is not None:
            first_node = previous_node.next
            second_node = first_node.next
            first_node.next = second_node.next
            second_node.next = first_node
            previous_node.next = second_node
            previous_node = first_node

        self.head = dummy_node.next

    def rotate_right(self, k):
        if self.head is None or self.head.next is None or k == 0:
            return
        if k < 0:
            raise ValueError("k must be non-negative")

        length = 1
        tail_node = self.head
        while tail_node.next is not None:
            tail_node = tail_node.next
            length += 1

        k %= length
        if k == 0:
            return

        tail_node.next = self.head
        new_tail = self.head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        self.head = new_tail.next
        new_tail.next = None

    def sort_merge(self):
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        if head is None or head.next is None:
            return head

        slow_node = head
        fast_node = head.next
        while fast_node is not None and fast_node.next is not None:
            slow_node = slow_node.next
            fast_node = fast_node.next.next

        second_head = slow_node.next
        slow_node.next = None
        left_head = self._merge_sort(head)
        right_head = self._merge_sort(second_head)
        return self._merge_nodes(left_head, right_head)

    @staticmethod
    def _merge_nodes(first_head, second_head):
        dummy_node = Node(0)
        current_node = dummy_node

        while first_head is not None and second_head is not None:
            if first_head.data <= second_head.data:
                current_node.next = first_head
                first_head = first_head.next
            else:
                current_node.next = second_head
                second_head = second_head.next
            current_node = current_node.next

        current_node.next = first_head if first_head is not None else second_head
        return dummy_node.next

    def add_one(self):
        carry = self._add_one_recursive(self.head)
        if carry:
            new_head = Node(carry)
            new_head.next = self.head
            self.head = new_head

    def _add_one_recursive(self, current_node):
        if current_node.next is None:
            current_node.data += 1
            if current_node.data == 10:
                current_node.data = 0
                return 1
            return 0

        carry = self._add_one_recursive(current_node.next)
        if carry:
            current_node.data += 1
            if current_node.data == 10:
                current_node.data = 0
                return 1
        return 0


class MultilevelDoublyList:
    @staticmethod
    def flatten(head):
        if head is None:
            return None

        current_node = head
        while current_node is not None:
            if current_node.child is None:
                current_node = current_node.next
                continue

            child_head = current_node.child
            next_node = current_node.next
            child_tail = MultilevelDoublyList.flatten(child_head)
            current_node.next = child_head
            child_head.previous = current_node
            current_node.child = None

            if next_node is not None:
                child_tail.next = next_node
                next_node.previous = child_tail
            current_node = child_tail

        return head


class RandomList:
    @staticmethod
    def copy_with_constant_space(head):
        if head is None:
            return None

        current_node = head
        while current_node is not None:
            copy_node = RandomNode(current_node.data)
            copy_node.next = current_node.next
            current_node.next = copy_node
            current_node = copy_node.next

        current_node = head
        while current_node is not None:
            copy_node = current_node.next
            if current_node.random is not None:
                copy_node.random = current_node.random.next
            current_node = copy_node.next

        current_node = head
        copied_head = head.next
        while current_node is not None:
            copy_node = current_node.next
            current_node.next = copy_node.next
            if copy_node.next is not None:
                copy_node.next = copy_node.next.next
            current_node = current_node.next

        return copied_head


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.head is None:
            raise IndexError("dequeue from empty queue")
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data

    def is_empty(self):
        return self.head is None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_left(self, data):
        new_node = DoublyNode(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.previous = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def append_right(self, data):
        new_node = DoublyNode(data)
        new_node.previous = self.tail
        if self.tail is not None:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def pop_left(self):
        if self.head is None:
            raise IndexError("pop from empty deque")
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.previous = None
        return data

    def pop_right(self):
        if self.tail is None:
            raise IndexError("pop from empty deque")
        data = self.tail.data
        self.tail = self.tail.previous
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return data


class LFUNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.frequency = 1


class LFUCache:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self.minimum_frequency = 0
        self.nodes = {}
        self.frequency_lists = defaultdict(OrderedDict)

    def _touch(self, node):
        frequency = node.frequency
        del self.frequency_lists[frequency][node.key]
        if not self.frequency_lists[frequency]:
            del self.frequency_lists[frequency]
            if self.minimum_frequency == frequency:
                self.minimum_frequency += 1

        node.frequency += 1
        self.frequency_lists[node.frequency][node.key] = node

    def get(self, key):
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self._touch(node)
        return node.value

    def put(self, key, value):
        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self._touch(node)
            return

        if len(self.nodes) == self.capacity:
            least_recent_key, _ = self.frequency_lists[self.minimum_frequency].popitem(last=False)
            del self.nodes[least_recent_key]

        node = LFUNode(key, value)
        self.nodes[key] = node
        self.frequency_lists[1][key] = node
        self.minimum_frequency = 1


def josephus(n, k):
    if n <= 0 or k <= 0:
        raise ValueError("n and k must be positive")

    head = Node(1)
    current_node = head
    for value in range(2, n + 1):
        current_node.next = Node(value)
        current_node = current_node.next
    current_node.next = head

    previous_node = current_node
    current_node = head
    while current_node.next is not current_node:
        for _ in range(k - 1):
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = current_node.next
        current_node = previous_node.next

    return current_node.data


if __name__ == "__main__":
    linked_list = LinkedList()
    for value in [1, 2, 3, 4, 5]:
        linked_list.insert(value)
    linked_list.reverse_recursive()
    assert linked_list.values() == [5, 4, 3, 2, 1]

    sorted_list = LinkedList()
    for value in [1, 1, 2, 3, 3]:
        sorted_list.insert(value)
    sorted_list.remove_duplicates_sorted()
    assert sorted_list.values() == [1, 2, 3]

    unsorted_list = LinkedList()
    for value in [3, 1, 3, 2, 1]:
        unsorted_list.insert(value)
    unsorted_list.remove_duplicates_unsorted()
    assert unsorted_list.values() == [3, 1, 2]

    sublist = LinkedList()
    for value in [1, 2, 3, 4, 5]:
        sublist.insert(value)
    sublist.reverse_sublist(2, 4)
    assert sublist.values() == [1, 4, 3, 2, 5]

    pairs = LinkedList()
    for value in [1, 2, 3, 4, 5]:
        pairs.insert(value)
    pairs.swap_pairs()
    assert pairs.values() == [2, 1, 4, 3, 5]

    rotated = LinkedList()
    for value in [1, 2, 3, 4, 5]:
        rotated.insert(value)
    rotated.rotate_right(2)
    assert rotated.values() == [4, 5, 1, 2, 3]

    unsorted_values = LinkedList()
    for value in [4, 2, 1, 3]:
        unsorted_values.insert(value)
    unsorted_values.sort_merge()
    assert unsorted_values.values() == [1, 2, 3, 4]

    number = LinkedList()
    for value in [1, 2, 9]:
        number.insert(value)
    number.add_one()
    assert number.values() == [1, 3, 0]

    random_one = RandomNode(1)
    random_two = RandomNode(2)
    random_one.next = random_two
    random_one.random = random_two
    random_two.random = random_one
    copied = RandomList.copy_with_constant_space(random_one)
    assert copied is not random_one
    assert copied.random is copied.next
    assert copied.next.random is copied

    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    assert queue.dequeue() == 10

    deque = Deque()
    deque.append_left(2)
    deque.append_left(1)
    deque.append_right(3)
    assert deque.pop_left() == 1
    assert deque.pop_right() == 3

    lfu_cache = LFUCache(2)
    lfu_cache.put(1, 1)
    lfu_cache.put(2, 2)
    assert lfu_cache.get(1) == 1
    lfu_cache.put(3, 3)
    assert lfu_cache.get(2) == -1
    assert lfu_cache.get(3) == 3

    assert josephus(5, 2) == 3
    print("all advanced linked-list checks passed")
