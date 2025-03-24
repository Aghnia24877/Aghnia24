class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class StackDoubleLinkedList:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = DNode(item)
        if self.top:
            new_node.prev = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack kosong!")
            return None
        item = self.top.data
        self.top = self.top.prev
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

# Contoh Penggunaan
stack = StackDoubleLinkedList()
stack.push(50)
stack.push(150)
stack.push(250)
stack.push(350)

print("Top stack:", stack.peek())
print("Pop:", stack.pop())
print("Pop:", stack.pop())