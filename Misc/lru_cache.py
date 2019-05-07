class Node:
	def __init__(self, key, value):
		self.prev = None
		self.next = None
		self.value = value
		self.key = key


# Head is least recently used
# Tail is most recently used
class LRUCache:
	def __init__(self, capacity):
		self.capacity = capacity
		self.size = 0
		self.map = {}
		self.head = None
		self.tail = None

	def set(self, k, v):
		# Check if it's already there
		# If so update entry
		elem = self.map.get(k)
		if elem is not None:
			self.map[k] = v
			return

		# First element
		if self.head is None:
			self.head = v
			self.tail = self.head
			self.map[k] = self.head
			self.size += 1
			return

		# Invalidate LRU aka evict head node
		if self.size >= self.capacity:
			self.map[self.head.key] = None
			new_head = self.head.next
			self.head.next = None
			new_head.prev = None
			self.head = new_head
			self.size -= 1

		# add to map
		self.map[k] = v
		self.tail.next = v
		v.prev = self.tail
		self.tail = v
		self.size += 1

	def get(self, k):
		# Get node from the hashmap
		n = self.map.get(k)
		if n is None:
			return None

		# Remove the node
		prev = n.prev
		next = n.next
		# check if it is head node
		if prev is not None:
			prev.next = next
		if next is not None:
			next.prev = prev

		# Add it to the tail
		self.tail.next = n
		n.prev = self.tail
		self.tail = n

		return n		

# Test cases
def main():
	lru_cache = LRUCache(3)
	n1 = Node(1, "A")
	n2 = Node(2, "B")
	n3 = Node(3, "C")
	n4 = Node(4, "D")

	lru_cache.set(1, n1)
	r1p = lru_cache.get(1)
	print(r1p.value)
	lru_cache.set(2, n2)
	lru_cache.set(3, n3)
	lru_cache.set(4, n4)

	r1 = lru_cache.get(1)
	r2 = lru_cache.get(2)
	r3 = lru_cache.get(3)
	r4 = lru_cache.get(4)
	r5 = lru_cache.get(1)

	print(r1)
	print(r2.value)
	print(r3.value)
	print(r4.value)
	print(r5)

main()