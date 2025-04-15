import math


class MinHeap:
    def __init__(self, values):
        self.heap = []
        self.buildHeap(values)

    def buildHeap(self, array):
        for index in array:
            self.insert(index)

    def parent(self, i):
        return math.floor((i - 1) / 2)

    def leftSon(self, i):
        return (i * 2) + 1

    def rightSon(self, i):
        return (i * 2) + 2

    def swap(self, i, j):
        aux = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = aux

    def showHeap(self):
        print(self.heap)

    def peek_min(self):
        return self.heap[0]

    def extract_min(self):

        lastElementIndex = len(self.heap) - 1
        self.swap(0, lastElementIndex)
        del self.heap[lastElementIndex]

        current = 0

        self.heapify_down(current)

    def insert(self, value):
        # Adiciona no final da lista
        self.heap.append(value)
        currentIndex = len(self.heap) - 1

        self.heapify_up(currentIndex)

    def heapify_up(self, index):
        while index > 0:

            parentIndex = self.parent(index)

            if (self.heap[index] < self.heap[parentIndex]):
                self.swap(index, parentIndex)  # trocando o filho com o pai
                index = parentIndex  # atualizando o indice do 'filho'
            else:
                break

    def heapfiy_down(self, index):

        while self.leftSon(index) < len(self.heap):

            leftSon = self.leftSon(index)
            rightSon = self.rightSon(index)

            if rightSon < len(self.heap):
                smallest = leftSon if self.heap[leftSon] < self.heap[rightSon] else rightSon
            else:
                smallest = leftSon

            if (self.heap[index] > self.heap[smallest]):
                self.swap(index, smallest)
                index = smallest
            else:
                break


class MaxHeap:

    def __init__(self):
        self.heap = []

    def parent(self, index):
        return math.floor((index - 1) / 2)

    def leftSon(self, index):
        return (index * 2) + 1

    def rightSon(self, index):
        return (index * 2) + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def peek_max(self):
        return self.heap[0]

    def showHeap(self):
        print(self.heap)

    def heapify_up(self, index):

        while index > 0:

            parentIndex = self.parent(index)
            if self.heap[parentIndex] < self.heap[index]:
                self.swap(index, parentIndex)
                index = parentIndex
            else:
                break

    def heapify_down(self, index):

        while self.leftSon(index) < len(self.heap):
            leftSon = self.leftSon(index)
            rightSon = self.rightSon(index)

            biggest = leftSon

            if (rightSon < len(self.heap)):
                biggest = rightSon if self.heap[rightSon] > self.heap[leftSon] else leftSon

            if (self.heap[biggest] > self.heap[index]):
                self.swap(index, biggest)
                index = biggest
            else:
                break


myHeap = MinHeap([10, 20, 4, 3, 1, 9])

myMaxHeap = MaxHeap([10, 20, 4, 3, 1, 9])
myHeap.showHeap()
