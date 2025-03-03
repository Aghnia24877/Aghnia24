#a.Buat struktur node menggunakan class
class Node:
    def __init__(self, value):
        self.value = value #menyimpan nilai data dalam node
        self.next = None   #menunjuk node berikutnya    (default: None)
        self.prev = None   #menunjuk node sebelumnya    (default: None)

#Buat class DoubleLinkedList
class DoubleLinkedList:
    def __init__(self, value):
        new_node = Node(value)      # Membuat node baru dengan nilai awal
        self.head = new_node        # Head menunjuk ke node baru (node pertama)
        self.tail = new_node        # Tail menunjuk ke node yang sama (karena hanya satu node)
        self.length = 1             # Panjang list diinisialisasi dengan 1

#b.Fungsi append
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

#c.Fungsi pop
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return temp.value

    #d.Fungsi prepend
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    #e.Fungsi insert
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next

        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node  
        temp.next = new_node
        self.length += 1
        return True

    #f.Fungsi remove
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            removed_node = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            self.length -= 1
            return removed_node.value
        if index == self.length - 1:
            return self.pop()

        temp = self.head
        for _ in range(index):
            temp = temp.next

        temp.prev.next = temp.next
        temp.next.prev = temp.prev  
        self.length -= 1
        return temp.value

    # Fungsi print_list untuk menampilkan isi list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        print("None")  # Menambahkan None di akhir untuk tampilan lebih baik

my_list = DoubleLinkedList(30)
my_list.append(20)
my_list.prepend(25)
my_list.insert(1, 40)
my_list.remove(5)
my_list.print_list()