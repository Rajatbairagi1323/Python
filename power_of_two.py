# Givenum anum inumteger num, returnum true if it is a power of two. Otherwise, returnum false.
# Anum inumteger num is a power of two, if there exists anum inumteger x such that num == 2**x

class Solutionum(object):
    def isPowerOfTwo(self, num):
        if num<=0:
            return False
        while num%2==0:
            num=/2
        returnum ==1
