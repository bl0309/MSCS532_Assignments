import time
import pandas as pd
import matplotlib.pyplot as plt

# Array Implementation
class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.size = size

    def insert(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.data[index] = value

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.data[index] = None

    def access(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.data[index]

# Stack using Array
class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

# Queue using Circular Array
class Queue:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, value):
        if self.count == self.capacity:
            raise OverflowError("Queue full")
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise IndexError("Queue empty")
        value = self.data[self.front]
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return value

# Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def delete_value(self, value):
        if not self.head:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        cur = self.head
        while cur.next and cur.next.data != value:
            cur = cur.next
        if cur.next:
            cur.next = cur.next.next

# Benchmarking Function
def benchmark():
    results = []

    # Array
    arr = Array(1000)
    start = time.perf_counter()
    for i in range(1000):
        arr.insert(i, i)
    end = time.perf_counter()
    results.append({"Structure": "Array", "Operation": "Insert", "Time (ms)": round((end - start) * 1000, 4)})

    start = time.perf_counter()
    for i in range(1000):
        arr.access(i)
    end = time.perf_counter()
    results.append({"Structure": "Array", "Operation": "Access", "Time (ms)": round((end - start) * 1000, 4)})

    start = time.perf_counter()
    for i in range(1000):
        arr.delete(i)
    end = time.perf_counter()
    results.append({"Structure": "Array", "Operation": "Delete", "Time (ms)": round((end - start) * 1000, 4)})

    # Stack
    stack = Stack()
    start = time.perf_counter()
    for i in range(1000):
        stack.push(i)
    end = time.perf_counter()
    results.append({"Structure": "Stack", "Operation": "Push", "Time (ms)": round((end - start) * 1000, 4)})

    start = time.perf_counter()
    for i in range(1000):
        stack.pop()
    end = time.perf_counter()
    results.append({"Structure": "Stack", "Operation": "Pop", "Time (ms)": round((end - start) * 1000, 4)})

    # Queue
    queue = Queue(1000)
    start = time.perf_counter()
    for i in range(1000):
        queue.enqueue(i)
    end = time.perf_counter()
    results.append({"Structure": "Queue", "Operation": "Enqueue", "Time (ms)": round((end - start) * 1000, 4)})

    start = time.perf_counter()
    for i in range(1000):
        queue.dequeue()
    end = time.perf_counter()
    results.append({"Structure": "Queue", "Operation": "Dequeue", "Time (ms)": round((end - start) * 1000, 4)})

    # Linked List
    ll = LinkedList()
    start = time.perf_counter()
    for i in range(1000):
        ll.insert_end(i)
    end = time.perf_counter()
    results.append({"Structure": "Linked List", "Operation": "Insert End", "Time (ms)": round((end - start) * 1000, 4)})

    start = time.perf_counter()
    for i in range(1000):
        ll.delete_value(i)
    end = time.perf_counter()
    results.append({"Structure": "Linked List", "Operation": "Delete by Value", "Time (ms)": round((end - start) * 1000, 4)})

    return pd.DataFrame(results)

# Main
if __name__ == "__main__":
    df = benchmark()
    print("\nPart 2 - Data Structures Performance:\n")
    print(df.to_string(index=False))

    # Plot
    plt.figure(figsize=(12, 6))
    for structure in df['Structure'].unique():
        subset = df[df['Structure'] == structure]
        plt.bar(subset['Structure'] + " - " + subset['Operation'], subset['Time (ms)'])

    plt.xlabel("Data Structure and Operation")
    plt.ylabel("Time (ms)")
    plt.title("Performance of Elementary Data Structures")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()
