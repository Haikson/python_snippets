def quicksort(lst):
    m = lst[len(lst)//2]
    i, j = [], []
    for item in lst:
        if item <= m:
            l = len(i)
            i.append(item)
            if len(i) > 1:
                while l > 0 and i[l] < i[l-1]:
                    i[l], i[l-1] = i[l-1], i[l]
                    l -= 1
        else:
            l = len(j)
            j.append(item)
            if len(j) > 1:
                while l > 0 and j[l] < j[l-1]:
                    j[l], j[l-1] = j[l-1], j[l]
                    l -= 1
    i.append(m)
    i.extend(j)
    return i
