from utils.benchmark import *

class QuickFindUF(object):
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

    @benchmark
    def connected(self, p, q):
        return self.id[p] == self.id[q]

    @benchmark
    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]

        for e in range(len(self.id)):
            if self.id[e] == pid:
                self.id[e] = qid

if __name__ == '__main__':
    tree = random_tree(1000000)
    arr = QuickFindUF(arr=tree)
    
    print "are 300201 and 249061 connected?: "
    print arr.connected(300201, 249061)
    "union(300201, 249061): "
    arr.union(300201, 249061)
    print "are 300201 and 249061 connected?: "
    print arr.connected(300201, 249061)
