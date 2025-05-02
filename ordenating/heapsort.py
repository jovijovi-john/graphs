import math


class MaxHeap:
    def __init__(self, array=[]):
        self.heap = []
        if len(array) > 0:
            self.build_heap(array)

    def build_heap(self, array):
        # Forma otimizada: construir a heap em O(n) com o método "heapify bottom-up" -> Verificar depois
        for item in array:
            self.insert(item)

    def left(self, index):
        return (index * 2) + 1

    def right(self, index):
        return (index * 2) + 2

    def parent(self, index):
        return math.floor(((index - 1) / 2))

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, value):
        # adiciona no final e vai subindo até encontrar um maior que ele
        self.heap.append(value)
        index = len(self.heap) - 1
        self.heapify_up(index)

    def peek_max(self):
        return self.heap[0]

    def extract_max(self):

        current = 0
        element = self.heap[current]
        lastElementIndex = len(self.heap) - 1
        self.swap(current, lastElementIndex)
        del self.heap[lastElementIndex]

        self.heapify_down(current)

        return element

    def heapify_up(self, index):

        while (index > 0):
            current = self.heap[index]
            parentIndex = self.parent(index)
            parent = self.heap[parentIndex]

            if (current > parent):
                self.swap(index, parentIndex)
                index = parentIndex
            else:
                # se o pai for maior que o filho então é hora de parar
                break

    def heapify_down(self, current):

        while self.left(current) < len(self.heap):

            left = self.left(current)
            right = self.right(current)

            largest = left

            if right < len(self.heap):
                largest = left if self.heap[left] > self.heap[right] else right

            if self.heap[current] < self.heap[largest]:
                self.swap(current, largest)
                current = largest
            else:
                break

    def show(self):
        print(self.heap)


class MinHeap:
    def __init__(self, array):
        self.heap = []
        if (len(array) > 0):
            self.build_heap(array)

    def build_heap(self, array):
        for item in array:
            self.insert(item)

    def insert(self, item):
        self.heap.append(item)
        index = len(self.heap) - 1
        self.heapify_up(index)


class HeapSort:
    def __init__(self, array):
        self.array = array
        self.heap = MaxHeap(self.array)

    def sort(self):
        sorted_array = []

        for i in range(len(self.array)):
            sorted_array.append(self.heap.extract_max())

        return sorted_array


myArray = [5, 100, 3, 2, 9, 21, 48, 22, 44, 55, 1003, 900, 213, 923]
print(HeapSort(myArray).sort())
