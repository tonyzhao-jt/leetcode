class DLinkedList:
    def __init__(key, value):
        self.val = value
        self.prev = None
        self.next = None
        self.key = key


class LRU:
    def __init__(self, capacity):
        self.cache = dict()
        self.head = DLinkedList()
        self.tail = DLinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.moveToHead(node)
            return node
        else:
            return -1
    
    def put(self, key, value):
        if key not in self.cache:
            newNode = DLinkedList(key, value)
            self.addToHead(newNode)
            self.size += 1
            if self.size >= self.capacity:
                self.cache.pop(self.tail.prev.key)
                self.removeTail()
                self.size -= 1
        else:
            self.moveToHead(self.cache[key])
            self.cache[key].val = value

    def addToHead(self, node):
        originalHead = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = originalHead
        originalHead.prev = node
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)
    
    def removeTail(self):
        tailNode = self.tail.prev
        self.removeNode(tailNode)
