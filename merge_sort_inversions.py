# Python 3 merge sort in count inversions


class MergeSort:
    def __init__(self, arr, counter):
        self.counter = counter
        self.arr = arr

    def merge_sort(self, arr=None):
        if arr is None:
            arr = self.arr
        if len(arr) <= 1:
            return arr

        mid_point = int(len(arr) / 2)
        a = []

        self.merge(self.merge_sort(arr[0:mid_point]), self.merge_sort(arr[mid_point:]), a)
        return a

    def merge(self, arr1, arr2, merged):
        a = 0
        b = 0

        for i in range(len(arr1) + len(arr2)):
            if a < len(arr1) and b < len(arr2):
                if arr1[a] > arr2[b]:
                    merged.insert(i, arr2[b])
                    b += 1
                    self.counter = self.counter + len(arr1) - a
                else:
                    merged.insert(i, arr1[a])
                    a += 1
            else:
                if b < len(arr2):
                    merged.insert(i, arr2[b])
                    b += 1
                elif a < len(arr1):
                    merged.insert(i, arr1[a])
                    a += 1


if __name__ == '__main__':
    arr_count = int(input())
    arr = list(map(int, input().split(' ')))
    merge_sort = MergeSort(arr=arr, counter=0)
    a = merge_sort.merge_sort()
    # print(a)
    print(merge_sort.counter)