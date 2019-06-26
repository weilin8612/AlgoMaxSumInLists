import random

def AlgoN2one(lists):
    n = len(lists)
    maxsofar = 0
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += lists[j]
            maxsofar = max(maxsofar, sum)
    return maxsofar

if __name__ == "__main__":
    lists = [i for i in range(-10, 10)]
    random.shuffle(lists)
    print(lists)
    sum = AlgoN2one(lists)
    print(sum)