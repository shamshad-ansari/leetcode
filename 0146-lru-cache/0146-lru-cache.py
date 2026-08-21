class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        # Dummy Nodes
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add_front(self, node):
        first = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = first
        first.prev = node
    
    def move_to_front(self, node):
        self.remove(node)
        self.add_front(node)
    
    def remove_last(self):
        if self.head.next == self.tail:
            return None
        
        last = self.tail.prev
        self.remove(last)
        return last

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.dll = DLL()
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.dll.move_to_front(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.dll.move_to_front(node)
            return
        
        node = Node(key, value)
        self.cache[key] = node
        self.dll.add_front(node)

        if len(self.cache) > self.capacity:
            lru = self.dll.remove_last()
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)