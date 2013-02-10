from utils.benchmark import *

class QuickUnionUF(object):
    id = []

    def __init__(self, n=None, arr=None):
        if arr == None:
            self.id = self._constuct_array(n)
        else:
            self.id = arr

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

    def connected(self, p, q):
        '''check if they share the same root'''
        return self._get_root(p) == self._get_root(q)

    def union(self, p, q):
        '''change root of p to point to root of q'''
        i = self._get_root(p)
        j = self._get_root(q)
        self.id[i] = j


if __name__ == '__main__':
    arr = QuickUnionUF(100000)
    random_tree(arr)
    print "are 30001 and 2461 connected?: "
    print arr.connected(30001, 2461)
    "union(30001, 2461): "
    arr.union(30001, 2461)
    print "are 30001 and 2461 connected?: "
    print arr.connected(30001, 2461)


