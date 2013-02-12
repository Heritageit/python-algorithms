from utils.benchmark import *

class QuickUnionWeighted(object):
    id = []
    sz = [] # keep track on the number of objects of each tree

    def __init__(self, n=None, arr=None):
        if arr == None:
            self.id = self._constuct_array(n)
        else:
            self.id = arr
        self.sz = [0]*len(self.id) # faster than [0 for e in range(len(self.id)+1)]

    def _constuct_array(self, n):
        temp_arr = []
        for e in range(n):
            temp_arr.append(e)
        return temp_arr

    def _get_root(self, el):
        '''check parents pointer until reach root'''
        while el != self.id[el]:
            el = self.id[el]
        return el

    @benchmark
    def connected(self, p, q):
        '''check if they share the same root'''
        return self._get_root(p) == self._get_root(q)

    @benchmark
    def union(self, p, q):
        '''change root of p to point to root of q'''
        i = self._get_root(p)
        j = self._get_root(q)
        # check if the tree rooted at i is smaller than the one rooted at j
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]


class QuickUnionPathCompression(QuickUnionWeighted):
    def _get_root(self, el):
        '''get roots and flatten the tree by pointing the nodes to the root directly'''
        while el != self.id[el]:
            self.id[el] = self.id[self.id[el]] # point node to root id
            el = self.id[el]
        return el


if __name__ == '__main__':
    tree = random_tree(1000000)
    arr = QuickUnionWeighted(arr=tree)
    
    print "are 300201 and 249061 connected?: "
    print arr.connected(300201, 249061)
    "union(300201, 249061): "
    arr.union(300201, 249061)
    print "are 300201 and 249061 connected?: "
    print arr.connected(300201, 249061)

