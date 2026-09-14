import heapq


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


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

	def print_list(self):
		current_node = self.head
		while current_node is not None:
			print(current_node.data, end=" -> ")
			current_node = current_node.next
		print("None")

	def delete_node(self, data):
		if self.head is None:
			return

		if self.head.data == data:
			self.head = self.head.next
			return

		current_node = self.head
		while current_node.next is not None:
			if current_node.next.data == data:
				current_node.next = current_node.next.next
				return
			current_node = current_node.next

	def reverse(self):
		previous_node = None
		current_node = self.head

		while current_node is not None:
			next_node = current_node.next
			current_node.next = previous_node
			previous_node = current_node
			current_node = next_node

		self.head = previous_node

	def find_middle(self):
		slow_node = self.head
		fast_node = self.head

		while fast_node is not None and fast_node.next is not None:
			slow_node = slow_node.next
			fast_node = fast_node.next.next

		return None if slow_node is None else slow_node.data

	def find_kth_from_end(self, k):
		if k <= 0:
			raise ValueError("k must be a positive integer")

		fast_node = self.head
		for _ in range(k):
			if fast_node is None:
				raise ValueError("k is larger than the list length")
			fast_node = fast_node.next

		slow_node = self.head
		while fast_node is not None:
			slow_node = slow_node.next
			fast_node = fast_node.next

		return slow_node.data

	def has_cycle(self):
		slow_node = self.head
		fast_node = self.head

		while fast_node is not None and fast_node.next is not None:
			slow_node = slow_node.next
			fast_node = fast_node.next.next

			if slow_node is fast_node:
				return True

		return False

	def cycle_start(self):
		slow_node = self.head
		fast_node = self.head

		while fast_node is not None and fast_node.next is not None:
			slow_node = slow_node.next
			fast_node = fast_node.next.next

			if slow_node is fast_node:
				cycle_start_node = self.head
				while cycle_start_node is not slow_node:
					cycle_start_node = cycle_start_node.next
					slow_node = slow_node.next
				return cycle_start_node

		return None

	def remove_nth_from_end(self, n):
		if n <= 0:
			raise ValueError("n must be a positive integer")

		dummy_node = Node(0)
		dummy_node.next = self.head
		fast_node = dummy_node
		slow_node = dummy_node

		for _ in range(n + 1):
			if fast_node is None:
				raise ValueError("n is larger than the list length")
			fast_node = fast_node.next

		while fast_node is not None:
			fast_node = fast_node.next
			slow_node = slow_node.next

		slow_node.next = slow_node.next.next
		self.head = dummy_node.next

	@staticmethod
	def merge_two_sorted(list_one, list_two):
		dummy_node = Node(0)
		current_node = dummy_node

		while list_one is not None and list_two is not None:
			if list_one.data <= list_two.data:
				current_node.next = list_one
				list_one = list_one.next
			else:
				current_node.next = list_two
				list_two = list_two.next
			current_node = current_node.next

		current_node.next = list_one if list_one is not None else list_two
		return dummy_node.next

	@staticmethod
	def get_intersection_node(head_one, head_two):
		pointer_one = head_one
		pointer_two = head_two

		while pointer_one is not pointer_two:
			pointer_one = pointer_one.next if pointer_one else head_two
			pointer_two = pointer_two.next if pointer_two else head_one

		return pointer_one

	def is_palindrome(self):
		if self.head is None or self.head.next is None:
			return True

		slow_node = self.head
		fast_node = self.head
		while fast_node.next is not None and fast_node.next.next is not None:
			slow_node = slow_node.next
			fast_node = fast_node.next.next

		second_half = self._reverse_nodes(slow_node.next)
		first_node = self.head
		second_node = second_half
		is_same = True
		while second_node is not None:
			if first_node.data != second_node.data:
				is_same = False
				break
			first_node = first_node.next
			second_node = second_node.next

		slow_node.next = self._reverse_nodes(second_half)
		return is_same

	@staticmethod
	def _reverse_nodes(head):
		previous_node = None
		current_node = head
		while current_node is not None:
			next_node = current_node.next
			current_node.next = previous_node
			previous_node = current_node
			current_node = next_node
		return previous_node

	@staticmethod
	def add_two_numbers(head_one, head_two): #important we need to see this 
		dummy_node = Node(0)
		current_node = dummy_node
		carry = 0

		while head_one is not None or head_two is not None or carry:
			value_one = head_one.data if head_one is not None else 0
			value_two = head_two.data if head_two is not None else 0
			total = value_one + value_two + carry
			carry = total // 10
			current_node.next = Node(total % 10)
			current_node = current_node.next
			head_one = head_one.next if head_one is not None else None
			head_two = head_two.next if head_two is not None else None

		return dummy_node.next

	def reorder(self):
		if self.head is None or self.head.next is None:
			return

		slow_node = self.head
		fast_node = self.head
		while fast_node.next is not None and fast_node.next.next is not None:
			slow_node = slow_node.next
			fast_node = fast_node.next.next

		second_half = self._reverse_nodes(slow_node.next)
		slow_node.next = None
		first_node = self.head
		while second_half is not None:
			first_next = first_node.next
			second_next = second_half.next
			first_node.next = second_half
			second_half.next = first_next
			first_node = first_next
			second_half = second_next
#    '''
#    1. Find the middle
#        ↓
# 2. Reverse the second half
#        ↓
# 3. Merge/zip the two halves alternately
#    '''
   

	@staticmethod
	def copy_random_list(head): #important
		if head is None:
			return None

		old_to_new = {}
		current_node = head
		while current_node is not None:
			old_to_new[current_node] = RandomNode(current_node.data)
			current_node = current_node.next

		current_node = head
		while current_node is not None:
			copy_node = old_to_new[current_node]
			copy_node.next = old_to_new.get(current_node.next)
			copy_node.random = old_to_new.get(current_node.random)
			current_node = current_node.next

		return old_to_new[head]

	@staticmethod
	def reverse_k_group(head, k):
		if k <= 0:
			raise ValueError("k must be a positive integer")

		dummy_node = Node(0)
		dummy_node.next = head
		group_previous = dummy_node

		while True:
			group_end = group_previous
			for _ in range(k):
				group_end = group_end.next
				if group_end is None:
					return dummy_node.next

			group_next = group_end.next
			previous_node = group_next
			current_node = group_previous.next
			while current_node is not group_next:
				next_node = current_node.next
				current_node.next = previous_node
				previous_node = current_node
				current_node = next_node

			old_group_start = group_previous.next
			group_previous.next = group_end
			group_previous = old_group_start

	@staticmethod
	def merge_k_sorted(lists):
		heap = []
		for list_index, head in enumerate(lists):
			if head is not None:
				heapq.heappush(heap, (head.data, list_index, head))

		dummy_node = Node(0)
		current_node = dummy_node
		while heap:
			_, list_index, smallest_node = heapq.heappop(heap)
			current_node.next = smallest_node
			current_node = current_node.next
			if smallest_node.next is not None:
				heapq.heappush(heap, (smallest_node.next.data, list_index, smallest_node.next))

		return dummy_node.next


class DoublyNode:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.previous = None
		self.next = None


class LRUCache:
	def __init__(self, capacity):
		if capacity <= 0:
			raise ValueError("capacity must be positive")
		self.capacity = capacity
		self.cache = {}
		self.head = DoublyNode(0, 0)
		self.tail = DoublyNode(0, 0)
		self.head.next = self.tail
		self.tail.previous = self.head

	def _remove(self, node):
		node.previous.next = node.next
		node.next.previous = node.previous

	def _add_to_front(self, node):
		node.next = self.head.next
		node.previous = self.head
		self.head.next.previous = node
		self.head.next = node

	def get(self, key):
		if key not in self.cache:
			return -1

		node = self.cache[key]
		self._remove(node)
		self._add_to_front(node)
		return node.value

	def put(self, key, value):
		if key in self.cache:
			self._remove(self.cache[key])

		node = DoublyNode(key, value)
		self.cache[key] = node
		self._add_to_front(node)

		if len(self.cache) > self.capacity:
			least_recent_node = self.tail.previous
			self._remove(least_recent_node)
			del self.cache[least_recent_node.key]


linked_list = LinkedList()
linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)

print("Original list:")
linked_list.print_list()

print("Middle:", linked_list.find_middle())
print("2nd node from end:", linked_list.find_kth_from_end(2))
print("Has cycle:", linked_list.has_cycle())

cyclic_list = LinkedList()
cyclic_list.insert(1)
cyclic_list.insert(2)
cyclic_list.insert(3)
cyclic_list.head.next.next.next = cyclic_list.head.next
print("Cyclic list has cycle:", cyclic_list.has_cycle())

linked_list.reverse()
print("Reversed list:")
linked_list.print_list()

linked_list.delete_node(20)
linked_list.print_list()
