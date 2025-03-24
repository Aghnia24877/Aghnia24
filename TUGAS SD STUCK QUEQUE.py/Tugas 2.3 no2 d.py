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

print("Input pertama")
pq = PriorityQueue()
pq.enqueue(2, 100)
pq.enqueue(1, 200)
pq.enqueue(3, 50)
pq.dequeue()
pq.dequeue()
pq.dequeue()

print("\nInput kedua")
pq = PriorityQueue()
pq.enqueue(5, 10)
pq.enqueue(3, 10)
pq.enqueue(4, 20)
pq.dequeue()
pq.dequeue()
pq.dequeue()

print("==================================================")
