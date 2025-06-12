import matplotlib.pyplot as plt
import time
import random

# Task class and priority queue implementation
class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"Task(id={self.task_id}, priority={self.priority})"

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if self.is_empty():
            return None
        self._swap(0, len(self.heap) - 1)
        max_task = self.heap.pop()
        self._heapify_down(0)
        return max_task

    def increase_key(self, index, new_priority):
        if new_priority < self.heap[index].priority:
            return
        self.heap[index].priority = new_priority
        self._heapify_up(index)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self._swap(index, parent)
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        n = len(self.heap)
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

# Benchmarking and graph generation
sizes = [100, 500, 1000, 2000, 4000]
times = []

for size in sizes:
    pq = PriorityQueue()
    tasks = [Task(task_id=i, priority=random.randint(1, 10000), arrival_time=0, deadline=100) for i in range(size)]
    
    start_time = time.perf_counter()
    for task in tasks:
        pq.insert(task)
    while not pq.is_empty():
        pq.extract_max()
    end_time = time.perf_counter()
    
    times.append(end_time - start_time)

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(sizes, times, marker='o', color='green')
plt.title("Priority Queue Runtime vs Number of Tasks")
plt.xlabel("Number of Tasks")
plt.ylabel("Execution Time (seconds)")
plt.grid(True)
plt.tight_layout()
plt.show()
