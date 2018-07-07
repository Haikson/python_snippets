'''
@author Kamo Petrosyan
Программа принимает на ход данные в виде:
n m: количество отрезков и точек
x1 x2: n строк с координатами отрезков на линии
y1 ... ym: m точек на линии через пробел.
возвращает количество, скольким отрезкам принадлежит точка

Ограничения:
    количество отрезков и точек от 1 до 50000
    значения любых координат не превышают 10^8 по модулю
    время выполнения не более 3 сек
    память не более 250 мб.
'''
import random
from bisect import bisect_left, bisect_right

def qsort(nums, key=None):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q] if key is None else [n for n in nums if key(n) < key(q)]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q] if key is None else [n for n in nums if key(n) > key(q)]
    return qsort(l_nums, key) + e_nums + qsort(b_nums, key)


def points_on_lines():
    m, n = map(int, input().split(' '))
    lines = []
    for i in range(m):
        lines.append(list(map(int, input().split(' '))))

    l_lines = qsort([l[0] for l in lines])
    # l_lines = sorted([l[0] for l in lines])
    r_lines = qsort([l[1] for l in lines])
    # r_lines = sorted([l[1] for l in lines])


    points = list(map(int, input().split(' ')))
    res = []

    for point in points:
        cnt = bisect_right(l_lines, point) - bisect_left(r_lines, point)
        res.append(cnt)
    return ' '.join(map(str, res))


if __name__ == '__main__':
    print(points_on_lines())
    # print(qsort([(2,3), (1,3),(4,7)], key=lambda x: x[0]))
