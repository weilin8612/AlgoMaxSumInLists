import random

def AlgoN3(lists):
    n = len(lists)
    maxsofar = 0
    for i in range(n):
        for j in range(i,n):
            sum = 0
            for k in range(i,j+1):
                sum += lists[k]
            maxsofar = max(maxsofar,sum)
    return maxsofar

if __name__ == "__main__":
    lists = [i for i in range(-10, 10)]
    random.shuffle(lists)
    print(lists)
    sum = AlgoN3(lists)
    print(sum)