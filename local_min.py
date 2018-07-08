from unittest import TestCase, main


def local_min(arr, row=0, col=0, m=None, n=0):
    n = len(arr) if n == 0 else n

    if m is None:
        m = min(arr[row])
        col = arr[row].index(m)

    if col < n - 2:
        if arr[row][col+1] < m:
            m = arr[row][col+1]
            col += 1
            return local_min(arr, row, col, m, n)
    if col > 0:
        if arr[row][col-1] < m:
            m = arr[row][col-1]
            col -= 1
            return local_min(arr, row, col, m, n)
    if row > 0:
        if arr[row-1][col] < m:
            row -= 1
            m = arr[row][col]
            return local_min(arr, row, col, m, n)
    if row < n - 1:
        if arr[row+1][col] < m:
            row += 1
            m = arr[row][col]
            return local_min(arr, row, col, m, n)
    return row, col


class TestLocalMin(TestCase):
    def setUp(self):
        self.arr = [
            [93, 60, 51, 70, 370],
            [88, 52, 34, 86, 89],
            [53, 51, 32, 95, 90],
            [53, 1, 19, 36, 94],
            [53, 17, 74, 25, 3],
            [80, 81, 54, 7, 67]
        ]

        self.arr1 = [
            [93, 60],
            [88, 52],
        ]
        self.arr2 = [
            [93, 60, 51],
            [88, 52, 34],
            [3, 5, 32],
        ]
        self.arr3 = [
            [93, 60, 51],
            [88, 52, 34],
            [53, 1, 32],
        ]

    def test_local_min(self):
        self.assertTupleEqual(local_min(self.arr), (3, 1))
        self.assertTupleEqual(local_min(self.arr1), (1, 1))
        self.assertTupleEqual(local_min(self.arr2), (2, 0))
        self.assertTupleEqual(local_min(self.arr3), (2, 1))


if __name__ == '__main__':
    main()


