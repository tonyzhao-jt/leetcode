class DLinkList:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = DLinkList()
        self.tail = DLinkList()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            self.moveToHead(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            new_node = DLinkList(key, value)
            self.cache[key] = new_node
            self.addToHead(new_node)
            self.size += 1
            if self.size > self.capacity:
                self.size -= 1
                self.cache.pop(self.tail.prev.key)
                self.removeTail()
                
        else:
            self.moveToHead(self.cache[key])
            self.cache[key].val = value

    def addToHead(self, node):
        origin_head = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = origin_head
        origin_head.prev = node
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        tail_node = self.tail.prev
        self.removeNode(tail_node)


