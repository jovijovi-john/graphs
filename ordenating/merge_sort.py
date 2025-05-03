class MergeSort:
    def __init__(self, array):
        self.array = array
        self.array = self.divide(self.array)

    def merge(self, left: list, right: list):

        merged_list = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if (left[i] < right[j]):
                merged_list.append(left[i])
                i += 1
            else:
                merged_list.append(right[j])
                j += 1

        while i < len(left):
            merged_list.append(left[i])
            i += 1

        while j < len(right):
            merged_list.append(right[j])
            j += 1

        return merged_list

    def divide(self, array):

        if len(array) <= 1:
            return array

        mid = len(array) // 2

        left = self.divide(array[:mid])
        right = self.divide(array[mid:])

        return self.merge(left, right)


sort = MergeSort([31, 92, 52, 12])
print(sort.array)
