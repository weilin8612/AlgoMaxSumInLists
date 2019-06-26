import random

def Algon1(lists):
    n = len(lists)
    maxsofar = 0
    maxendinghere = 0
    for i in range(n):
        maxendinghere = max(maxendinghere + lists[i], 0)
        maxsofar = max(maxendinghere, maxsofar)
    return maxsofar

if __name__ == "__main__":
    lists = [i for i in range(-10, 10)]
    random.shuffle(lists)
    print(lists)
    sum = Algon1(lists)
    print(sum)
