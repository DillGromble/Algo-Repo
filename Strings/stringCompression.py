#------------------------------------------------------------------------------#
# Given a string, return a compressed string using the counts of repeated      #
# characters.  For instance 'aaabcccccaa' == 'a3b1c5a2'.  If the length of the #
# compressed string is not shorter than the original, return the original.     #
# Time complexity O(n)                                                         #
#                                                                              #
#     @param s : string                                                        #
#     @return: string                                                          #
#------------------------------------------------------------------------------#

def stringCompression(s):
  ans = ''
  idx = 0

  while idx < len(s):
    char = s[idx]
    cnt = 1

    while idx < len(s)-1 and s[idx+1] == char:
      cnt += 1
      idx += 1

    idx += 1
    ans += char + str(cnt)

  return ans if len(ans) < len(s) else s

print(stringCompression('aaabcccccaabefgggggga'))
