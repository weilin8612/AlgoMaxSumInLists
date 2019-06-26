import random
# import sys
#
# sys.setrecursionlimit(1000000)

def logn(left, right, lists):
    if right == left:
        return max(lists[left], 0)
    if left > right :
        return 0

    middle = (left + right)//2
    #print("middle is" + str(middle))
    #中间的数列，求最大值
    #先求middle为边界的左面的最大值
    maxmiddleleft = 0
    index = middle
    maxsum = 0
    while index >= left:
        maxsum += lists[index]
        maxmiddleleft = max(maxmiddleleft, maxsum)
        index -= 1

    #再求middle为边界的右面的最大值
    maxmiddleright = 0
    index = middle+1
    maxsum = 0
    while index <= right:
        maxsum += lists[index]
        maxmiddleright = max(maxmiddleright, maxsum)
        index += 1

    #把贴近边界两边的最大值合并起来，就是middle处的最大值
    maxmiddle = maxmiddleleft + maxmiddleright
    # print("maxmiddle is" + str(maxmiddle))
    #左面的数列，求最大值
    # print("准备调用左面logn" + str(left) +"," + str(middle))
    maxleft = logn(left, middle, lists)
    # print("准备调用右面logn" + str(middle) + "," + str(right))
    #右面的数列，求最大值
    maxright = logn(middle+1, right, lists)

    maxresult = max(maxleft, maxmiddle, maxright)
    return maxresult


def Algologn(lists):
    n = len(lists)
    return logn(0, n-1, lists)

if __name__ == "__main__":
    lists = [i for i in range(-10, 10)]
    random.shuffle(lists)
    print(lists)
    sum = Algologn(lists)
    print(sum)
