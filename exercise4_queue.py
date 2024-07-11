#4
class MyQueue:
  def __init__(self, capacity):
    self.capacity = capacity
    self.queue = []

  def is_empty(self):
    return len(self.queue) == 0

  def is_full(self):
    return len(self.queue) == self.capacity

  def dequeue(self):
    if self.is_empty():
      raise IndexError("Queue is empty")
    return self.queue.pop(0)

  def enqueue(self, item):
    if self.is_full():
      raise IndexError("Queue is full")
    self.queue.append(item)

  def front(self):
    if self.is_empty():
      raise IndexError("Queue is empty")
    return self.queue[0]

queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
queue1.enqueue(2)
print(queue1.is_full())
print(queue1.front())
print(queue1.dequeue())
print(queue1.front())
print(queue1.dequeue())
print(queue1.is_empty())