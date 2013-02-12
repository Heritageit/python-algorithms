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

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]

        for e in range(len(self.id)):
            if self.id[e] == pid:
                self.id[e] = qid

if __name__ == '__main__':
    from test_quickalgo import test
    tree = random_tree(1000000)
    arr = [QuickFindUF]
    test(arr, tree)

