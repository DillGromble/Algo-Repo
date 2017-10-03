#------------------------------------------------------------------------------#
# Given an array of integers, determine if any 3 of the numbers sum to 0.      #
# Each number should only be used once.                                        #
# Time complexity O(n^2)                                                       #
#                                                                              #
#     @param nums : array                                                      #
#     @return: 2dArray(all answers)                                            #
#------------------------------------------------------------------------------#

'''
The main trick here is to sort the array.
Once sorted, we can iterate through the array and use the method from the 2sum
problem on everything to the right of the current index.
'''

def threeSum(self, nums):
  nums.sort()
  ans = []

  # we only need to iterate to len-2: when index is len-3 we are out of options
  for i in range(len(nums)-2):

    # if we've already seen the number at the index, just skip the logic
    if i == 0 or nums[i] != nums[i-1]:
      l, h = i+1, len(nums)-1
      while l < h:
        s = nums[i] + nums[l] + nums[h]
        if s < 0: l += 1
        elif s > 0: h -= 1
        else:
          ans.append([nums[i], nums[l], nums[h]])

          # if next l or h is the same as the last, keep skipping until its not
          while l < h and nums[l] == nums[l+1]: l += 1
          while l < h and nums[h] == nums[h-1]: h -= 1
          l += 1
          h -= 1

  return ans
