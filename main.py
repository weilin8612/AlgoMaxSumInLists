from algorithm_four_test.n3 import AlgoN3
from algorithm_four_test.n2one import AlgoN2one
from algorithm_four_test.n2two import AlgoN2two
from algorithm_four_test.logn import Algologn
from algorithm_four_test.n1 import Algon1
import random
from time import ctime,time

lists = [i for i in range(-1000, 1001)]
random.shuffle(lists)

for i in ('AlgoN3(lists)', 'AlgoN2one(lists)', 'AlgoN2two(lists)', 'Algologn(lists)', 'Algon1(lists)'):
    start = time()
    print("start {0} is {1}".format(i, ctime()))
    maxsofar = eval(i)
    print("stop {0} is {1}".format(i, ctime()) )
    stop = time()
    print("{0} runing time is {1}".format(i, stop - start))
    print("result is {}".format(maxsofar))

# maxsofar = AlgoN2one(lists)
# print(maxsofar)
#
# maxsofar = AlgoN2two(lists)
# print(maxsofar)
#
# maxsofar = Algologn(lists)
# print(maxsofar)
#
# maxsofar = Algon1(lists)
# print(maxsofar)