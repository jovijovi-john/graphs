class MergeSort:
    def __init__(self, array):
        self.array = array
        self.array = self.divide(self.array)

    def merge(self, left: list, right: list):

        merged_list = []
        count_i = 0
        count_j = 0

        while count_i < len(left) and count_j < len(right):
            if (left[count_i] < right[count_j]):
                merged_list.append(left[count_i])
                count_i += 1
            else:
                merged_list.append(right[count_j])
                count_j += 1

        while count_i < len(left):
            merged_list.append(left[count_i])
            count_i += 1

        while count_j < len(right):
            merged_list.append(right[count_j])
            count_j += 1

        return merged_list

    def divide(self, array):

        if len(array) <= 1:
            return array

        mid = len(array) // 2

        left = self.divide(array[:mid])
        right = self.divide(array[mid:])

        return self.merge(left, right)


sort = MergeSort([31, 52, 92, 12, 27, 55, 2])
print(sort.array)
