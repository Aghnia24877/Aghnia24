class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1
    
    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue penuh")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
    
    def dequeue(self):
        if self.front == -1:
            print("Queue kosong")
            return None
        removed_item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return removed_item
    
    def display(self):
        if self.front == -1:
            return []
        result = []
        i = self.front
        while True:
            result.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size
        return result

# Uji coba Circular Queue dengan ukuran 5
cq1 = CircularQueue(5)
input3 = [1, 2, 3, 4, 5]
for item in input3:
    cq1.enqueue(item)
print("Circular Queue ukuran 5 setelah enqueue:", cq1.display())

# Uji coba Circular Queue dengan ukuran 7
cq2 = CircularQueue(7)
input4 = [10, 20, 30, 40, 50, 60, 70]
for item in input4:
    cq2.enqueue(item)
print("Circular Queue ukuran 7 setelah enqueue:", cq2.display())

# Uji kondisi saat queue penuh dan kosong
cq1.enqueue(6)  # Seharusnya penuh
for _ in range(5):
    cq1.dequeue()
print("Circular Queue ukuran 5 setelah semua elemen didequeue:", cq1.display())