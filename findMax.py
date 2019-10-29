#file -- consecutive.py --
import consecutive

def findMaxSubArray(treesList, n):
    sums = []
    for i in range(0, len(treesList)):
        result = consecutive.findtotalConsecutive(treesList, n, i)
        sums.append(result)

    max = sums[0]
    index = 0
    for m in range(0, len(sums)):
        if (max < sums[m]):
            max = sums[m]
            index = m

    return max, index

def findSecondMaxSubArray(treesList, firstResult, n):
    subArrayLeft = treesList[0:firstResult[0]]
    resultLeft = findMaxSubArray(subArrayLeft, n)
    print resultLeft

    subArrayRight = treesList[firstResult[1]:len(treesList)]
    resultRight = findMaxSubArray(subArrayRight, n)
    print resultRight

    if (resultLeft[0] > resultRight[0]):
        #print (resultLeft[0], firstResult[0])
        return (resultLeft[0], firstResult[0])

    #print (resultRight[0], firstResult[1])
    return (resultRight[0], firstResult[1])


def maximizeApplesPickedBetweenKandL(a, k, l):
    if ((k + l) > len(a)):
        return -1

    if(k >= l):
        resultK = findMaxSubArray(a, k)
        #print result
        resultL = findSecondMaxSubArray(a, tuple((resultK[1], k)), l)
    else:
        resultL = findMaxSubArray(trees, l)
        #print result
        resultK = findSecondMaxSubArray(a, tuple((resultL[1], l)), k)

    return (resultK, resultL)

treesInExample = [6, 1, 4, 6, 3, 2, 7, 4]

results = maximizeApplesPickedBetweenKandL(treesInExample, 3, 2)
print "overall result " + str(results) + " total: " + str(results[0][0] + results[1][0])
