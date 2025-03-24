import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        print(f"Before Enqueue: {self.queue}")
        heapq.heappush(self.queue, (priority, item))
        print(f"After Enqueue {item}, priority {priority}: {self.queue}")

    def dequeue(self):
        print(f"Before Dequeue: {self.queue}")
        item = heapq.heappop(self.queue)[1]
        print(f"After Dequeue {item}: {self.queue}")
        return item

# Uji coba dengan skenario pertama
pq1 = PriorityQueue()
input1 = [(2, 100), (1, 200), (3, 50)]
for priority, item in input1:
    pq1.enqueue(item, priority)

print("Hasil dequeue skenario pertama:")
while pq1.queue:
    pq1.dequeue()

# Uji coba dengan skenario kedua
pq2 = PriorityQueue()
input2 = [(5, 10), (3, 30), (4, 20)]
for priority, item in input2:
    pq2.enqueue(item, priority)

print("Hasil dequeue skenario kedua:")
while pq2.queue:
    pq2.dequeue()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = self.rear = None
    
    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
    
    def dequeue(self):
        if self.front is None:
            print("Queue kosong")
            return None
        removed_item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed_item
    
    def display(self):
        result = []
        temp = self.front
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result

# Uji coba Queue dengan Linked List
queue1 = QueueLinkedList()
input1 = [8, 16, 24, 32, 40]
for item in input1:
    queue1.enqueue(item)
print("Queue pertama setelah enqueue:", queue1.display())

queue2 = QueueLinkedList()
input2 = [11, 22, 33, 44, 55]
for item in input2:
    queue2.enqueue(item)
print("Queue kedua setelah enqueue:", queue2.display())

# Proses dequeue dan bandingkan hasilnya
for _ in range(3):
    queue1.dequeue()
    queue2.dequeue()
print("Queue pertama setelah 3 kali dequeue:", queue1.display())
print("Queue kedua setelah 3 kali dequeue:", queue2.display())