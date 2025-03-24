from collections import deque

class Deque:
    def __init__(self):
        self.deque = deque()

    def add_front(self, item):
        print(f"Before Add Front: {list(self.deque)}")
        self.deque.appendleft(item)
        print(f"After Add Front {item}: {list(self.deque)}")

    def add_rear(self, item):
        print(f"Before Add Rear: {list(self.deque)}")
        self.deque.append(item)
        print(f"After Add Rear {item}: {list(self.deque)}")

    def remove_front(self):
        print(f"Before Remove Front: {list(self.deque)}")
        item = self.deque.popleft()
        print(f"After Remove Front {item}: {list(self.deque)}")
        return item

    def remove_rear(self):
        print(f"Before Remove Rear: {list(self.deque)}")
        item = self.deque.pop()
        print(f"After Remove Rear {item}: {list(self.deque)}")
        return item

print("Input pertama")
dq = Deque()
dq.add_front(100)
dq.add_front(200)
dq.add_front(300)
dq.remove_front()
dq.remove_rear()

print("\nInput kedua")
dq = Deque()
dq.add_front(10)
dq.add_front(20)
dq.add_front(30)
dq.add_rear(40)
dq.add_rear(50)
dq.remove_front()
dq.remove_rear()

print("==================================================")
