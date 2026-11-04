# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l,r = 0,n
        if guess(n)==0:
            return n
        mid = n//2
        while guess(mid)!= 0:
            if guess(mid) == -1:#guess too high
                r = mid
                mid = (l+r)//2
            else:
                l = mid
                mid = (l+r)//2
        return mid