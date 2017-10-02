#------------------------------------------------------------------------------#
# Given a string, find the length of the longest substring without repeating   #
# characters.                                                                  #
# Time complexity O(n)                                                         #
#                                                                              #
#     @param s : string                                                        #
#     @return: integer(len of substring)                                       #
#------------------------------------------------------------------------------#

def lengthOfLongestSubstring(s):
  charsSeen = {}
  ans = 0
  start = 0

  for i in range(len(s)):
      char = s[i]
      if char in charsSeen and start <= charsSeen[char]:
          start = charsSeen[char] + 1
      else:
          ans = max(ans, i - start + 1)

      charsSeen[char] = i

  return ans
