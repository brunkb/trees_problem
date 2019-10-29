def findtotalConsecutive(trees, size, index):
    if (size > len(trees)):
        return -1

    max = 0
    sum = 0
    for i in range(0, size):
        if (index > len(trees) - 1):
            return -1
        sum += trees[index]
        index += 1
    return sum
