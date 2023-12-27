import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        # Priority is negated to create a min heap
        heapq.heappush(self.heap, (-priority, item))

    def pop(self):
        if not self.is_empty():
            _, item = heapq.heappop(self.heap)
            return item
        else:
            raise IndexError("pop from an empty priority queue")

    def top(self):
        if not self.is_empty():
            priority, item = self.heap[0]
            return item
        else:
            raise IndexError("top from an empty priority queue")

    def is_empty(self):
        return not bool(self.heap)

    def size(self):
        return len(self.heap)

# Example usage:
priority_queue = PriorityQueue()

priority_queue.push('Task A', 3)
priority_queue.push('Task B', 1)
priority_queue.push('Task C', 2)

print("Top priority task:", priority_queue.top())  # Output: Task B
print("Queue size:", priority_queue.size())  # Output: 3

while not priority_queue.is_empty():
    print("Processing task:", priority_queue.pop())
