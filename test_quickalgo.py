import time
import random
from copy import deepcopy
from utils.benchmark import *
from quickunion import *
from quickunion_weighted import *
from quickfind import *

# create only one array of id's so the comparison is fair
ids = [e for e in range(1000000)]

my_trees = [QuickFindUF, QuickUnionUF, 
        QuickUnionWeighted, QuickUnionPathCompression]

def test(classes, tree):
    for e in classes:
        tmp = e(arr=deepcopy(tree))
        print "%s:" % tmp.__class__.__name__
        t = time.clock()
        for i in range(10000):
            tmp.connected(random.choice(tree), random.choice(tree))
            tmp.union(random.choice(tree), random.choice(tree))
        print "Total time: {0} ".format(time.clock()-t)

if __name__ == '__main__':
    test(my_trees, ids)
