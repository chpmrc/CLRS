def findmaxcrossingsubarray(a, low, mid, high):
    summation = 0
    maxleftsum = None
    maxrightsum = None
    maxleftindex = None
    maxrightindex = None
    for i in range(mid, low - 1, -1):
        summation += a[i]
        if summation > maxleftsum:
            maxleftindex = i
            maxleftsum = summation
    summation = 0
    for j in range(mid + 1, high):
        summation += a[j]
        if summation > maxrightsum:
            maxrightindex = j
            maxrightsum = summation
    return (maxleftindex, maxrightindex, maxleftsum + maxrightsum)


def findmaxsubarray(a, low, high):
    pass  # TODO

changes = [1, -1, 2, 3, -5, 10, -10]
print(findmaxcrossingsubarray(changes, 0, len(changes) / 2, len(changes)))
