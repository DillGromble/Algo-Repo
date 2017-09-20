#------------------------------------------------------------------------------#
#   Find the number of possible paths from top left to bottom right a matrix   #
#     @param A : integer                                                       #
#     @param B : integer     where A and B are the end point goal coordinates  #
#     @return an integer     where return is the number of possible paths      #
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# DP solution:  This builds upon an assumption that the goal is right next to
# us, and adds up all the possibilities until we do find it.
#------------------------------------------------------------------------------#

def uniquePathsDP (A, B):
  '''
  2DA is filled with 1s to account for goal being on 1st row or column
  Alternatively, one can ask if i or j is 0 in the loop below and assign 1
  in that case
  '''
  numPaths = [[1 for x in xrange(B)] for y in xrange(A)]

  for i in xrange(1, A):
    for j in xrange(1, B):
      numPaths[i][j] = numPaths[i-1][j] + numPaths[i][j-1]

  return numPaths[-1][-1]



#------------------------------------------------------------------------------#
# Recursive solution: Opposite of DP, ask if we are 1 step away, if not call fn
# again with decremented ending points and add up answer
#------------------------------------------------------------------------------#

def uniquePathsRecursive (A, B):
  if A == 1 or B ==1: return 1
  return uniquePathsRecursive(A-1, B) + uniquePathsRecursive(A, B-1)



print('DP: ', uniquePathsDP(7, 3))
print('Recursive: ', uniquePathsRecursive(7, 3))
