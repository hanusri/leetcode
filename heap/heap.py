# implement a min heap in Python. It need not be zero-indexed. Lets insert from index 1

class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        self.heapify_up(self.size)

    def heapify_up(self, index):
        while index // 2 > 0:
            if self.heap[index] < self.heap[index // 2]:
                self.heap[index], self.heap[index // 2] = self.heap[index // 2], self.heap[index]
            index //= 2

    def delete(self):
        if self.size == 0:
            return
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.heapify_down(1)

    def heapify_down(self, index):
        while index * 2 <= self.size:
            min_child = self.min_child(index)
            if self.heap[index] > self.heap[min_child]:
                self.heap[index], self.heap[min_child] = self.heap[min_child], self.heap[index]
                index = min_child
            else:
                break

    def min_child(self, index):
        if index * 2 + 1 > self.size:
            return index * 2
        if self.heap[index * 2] < self.heap[index * 2 + 1]:
            return index * 2
        return index * 2 + 1
    
    def get_min(self):
        if self.size == 0:
            return
        return self.heap[1]

    def display(self):
        print(self.heap[1:])
    
    # implement heapify method which converts an array into a min heap
    def heapify(self, arr):
        self.size = len(arr)
        self.heap = [0] + arr
        index = self.size // 2
        while index > 0:
            self.heapify_down(index)
            index -= 1