import time
from copy import deepcopy
from utils.benchmark import *
from quickunion import *
from quickunion_weighted import *
from quickfind import *

# create only one array of id's so the comparison is fair
#ids = random_tree(1000000)

my_trees = [QuickFindUF, QuickUnionUF, 
        QuickUnionWeighted, QuickUnionPathCompression]

print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

def test(classes, tree):
    for e in classes:
        tmp = e(arr=deepcopy(tree))
        print "%s:" % tmp.__class__.__name__
        t = time.clock()
        print "\tare 300201 and 249061 connected?: %s" % tmp.connected(300201, 249061)
        "\tunion(300201, 24061): "
        tmp.union(300201, 249061)
        print "\tare 300201 and 24061 connected?: %s" % tmp.connected(300201, 249061)
        print "Total time: {0} ".format(time.clock()-t)

if __name__ == '__main__':
    test(my_trees, ids)
    #test([QuickUnionWeighted], ids)
