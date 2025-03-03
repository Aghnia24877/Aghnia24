class Node:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, nim, nama):
        new_node = Node(nim, nama)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def pop(self):
        if not self.tail:
            print("List is empty!")
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
    
    def prepend(self, nim, nama):
        new_node = Node(nim, nama)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def insert(self, index, nim, nama):
        if index == 0:
            self.prepend(nim, nama)
            return
        new_node = Node(nim, nama)
        temp = self.head
        for _ in range(index - 1):
            if not temp:
                print("Index out of range!")
                return
            temp = temp.next
        if not temp.next:
            self.append(nim, nama)
        else:
            new_node.next = temp.next
            new_node.prev = temp
            temp.next.prev = new_node
            temp.next = new_node
    
    def remove(self, nim):
        temp = self.head
        while temp:
            if temp.nim == nim:
                if temp == self.head:
                    self.head = temp.next
                    if self.head:
                        self.head.prev = None
                elif temp == self.tail:
                    self.tail = temp.prev
                    self.tail.next = None
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                return
            temp = temp.next
        print("NIM not found!")
    
    def display(self):
        temp = self.head
        while temp:
            print(f"NIM: {temp.nim}, Nama: {temp.nama}")
            temp = temp.next

if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.append("24091397001", "Varelera")
    dll.append("24091397009", "Nazzala")
    dll.append("24091397010", "Zaryan")
    dll.prepend("2409137011", "Alice")
    dll.prepend("24091397004", "Haruka")
    dll.insert(1,"24091397037", "Hildan")
    dll.display()
    print("\nSetelah Remove dan Pop:")
    dll.remove("24091397011.",)
    dll.pop()
    dll.display()
