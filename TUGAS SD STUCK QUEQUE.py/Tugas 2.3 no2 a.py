class QueueArray:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def display(self):
        return self.queue

# Uji coba queue biasa dengan array
queue1 = QueueArray()
input1 = [10, 20, 30, 40, 50]
for item in input1:
    queue1.enqueue(item)
print("Queue setelah enqueue input pertama:", queue1.display())

queue2 = QueueArray()
input2 = [5, 15, 25, 35, 45, 55]
for item in input2:
    queue2.enqueue(item)
print("Queue setelah enqueue input kedua:", queue2.display())

# Proses dequeue dan bandingkan hasilnya
for _ in range(3):
    queue1.dequeue()
    queue2.dequeue()
print("Queue pertama setelah 3 kali dequeue:", queue1.display())
print("Queue kedua setelah 3 kali dequeue:", queue2.display())