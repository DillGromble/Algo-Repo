#------------------------------------------------------------------------------#
# Given a sorted array of integers, count the number of occurances of a given  #
# integer.                                                                     #
#                                                                              #
# Time complexity O(logN)                                                      #
#                                                                              #
#     @param A : array                                                         #
#     @param B : int (to find)                                                 #
#     @return: int (num found)                                                 #
#------------------------------------------------------------------------------#


class countSortedArr:

    def findCount(self, A, B):
        first = self.binaryFind(A, B, True)
        if first == -1: return 0
        last = self.binaryFind(A, B, False)
        return last - first + 1

    def binaryFind(self, x, num, first):
        lo = 0
        hi = len(x) - 1
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if x[mid] == num:
                ans = mid
                if first: hi = mid - 1
                else: lo = mid + 1
            elif x[mid] < num:
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
