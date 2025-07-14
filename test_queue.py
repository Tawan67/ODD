class SimpleQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("dequeue from empty queue")
    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage
if __name__ == "__main__":
    q = SimpleQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())  # Output: 1
    print(q.size())     # Output: 2
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())