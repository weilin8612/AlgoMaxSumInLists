import random

def AlgoN2two(lists):
    n = len(lists)
    sums = [lists[0]]
    maxsofar = 0
    for i in range(1,n):
        mid = sums[i-1] + lists[i]
        sums.append(mid)
    for i in range(n):
        for j in range(i,n):
            sum = sums[j] - sums [i-1]
            maxsofar = max(maxsofar, sum)
    return maxsofar

if __name__ == "__main__":
    lists = [i for i in range(-10, 10)]
    random.shuffle(lists)
    print(lists)
    sum = AlgoN2two(lists)
    print(sum)