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


myHeap = MinHeap([10, 20, 4, 3, 1, 9])

myMaxHeap = MaxHeap([10, 20, 4, 3, 1, 9])
myHeap.showHeap()
