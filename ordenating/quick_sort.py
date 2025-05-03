class QuickSort:
    def __init__(self, array: list):
        self.array = array
        self.array = self.partition(self.array)
        print(self.array)

    def partition(self, array):

        if len(array) <= 1:
            return array

        pivot_index = len(array) // 2
        pivot = array[pivot_index]

        left = []
        right = []

        for i in range(len(array)):
            if i != pivot_index:
                if array[i] < pivot:
                    left.append(array[i])
                else:
                    right.append(array[i])

        left = self.partition(left)
        right = self.partition(right)

        return_array = left.copy()
        return_array.append(pivot)
        j = 0
        while j < len(right):
            return_array.append(right[j])
            j += 1

        return return_array


sort = QuickSort([10, 2, 50, 21, 84, 32])
