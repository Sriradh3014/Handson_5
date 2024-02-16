class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def build_min_heap(self, array):
        self.heap = array[:]
        for i in range(len(self.heap) // 2, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if l < len(self.heap) and self.heap[l] < self.heap[i]:
            smallest = l
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def get_min(self):
        if not self.heap:
            return None
        return self.heap[0]

    def pop_min(self):
        if not self.heap:
            return None
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify(0)
        return min_val


heap = MinHeap()
heap.build_min_heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
print("Min heap:", heap.heap)  
print("Minimum value:", heap.get_min())  
print("Popped minimum value:", heap.pop_min())  
print("Min heap after popping:", heap.heap)  