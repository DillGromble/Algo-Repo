#------------------------------------------------------------------------------#
# You are given a string. The only operation allowed is to insert characters in#
# the beginning of the string. How many minimum characters are needed to be    #
# inserted to make the string a palindrome string                              #
#                                                                              #
# Time complexity O(n)                                                         #
#                                                                              #
#     @param A : string                                                        #
#     @return: Int                                                             #
#                                                                              #
# Example:                                                                     #
#   Input: ABC                                                                 #
#   Output: 2                                                                  #
#   Input: AACECAAAA                                                           #
#   Output: 2                                                                  #
#------------------------------------------------------------------------------#

'''
This can be done in O(n) time using a trick with the lps(longest prefix suffix)
array.  If we generate a string that is the original string concatenated with
it's reverse(with some symbol to divide) we can then find the lps array for this
string.  The last number in the lps array can be subtracted from the len of the
original string to give your answer.

Example:
  lps('AACECAAAA:AAAACECAA') == [0, 1, 0, 0, 0, 1, 2, 2, 2, 0, 1, 2, 2, 2, 3, 4, 5, 6, 7]

  Since the longest prefix which is also a suffix at the last index is 7, we
  known that we have a distance of 2 between the original length of 9, and 7
'''



class palindromeEditDist:
    # @param A : string
    # @return an integer

    def solve(self, A):
        tester = A + ':' + A[::-1]
        lpsArr = self.lps(tester)
        return len(A) - lpsArr[-1]


    def lps(self, s):
      lpsArr = [None for x in range(len(s))]
      if len(s): lpsArr[0] = 0
      j, i = 0, 1

      while i < len(s):
        if s[i] == s[j]:
          lpsArr[i] = j+1
          i += 1
          j += 1
        else:
          if j != 0:
            j = lpsArr[j-1]
          else:
            lpsArr[i] = 0
            i += 1

      return lpsArr
