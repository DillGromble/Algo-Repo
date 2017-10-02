#------------------------------------------------------------------------------#
# Given 2 strings, determine if they can be made into the same string with one #
# edit (insert, remove, replace)                                               #
# Time complexity O(n)                                                         #
#                                                                              #
#     @param a : string                                                        #
#     @param b : string                                                        #
#     @return: Bool                                                            #
#------------------------------------------------------------------------------#

def oneAway(a, b):
  (short, long) = (a, b) if len(a) <= len(b) else (b, a)

  if len(long) - len(short) > 1:
    return False

  elif len(long) == len(short):
    foundDiff = False
    for i in range(len(long)):
      if long[i] != short[i]:
        if foundDiff:
          return False
        foundDiff = True

  else:
    for i in range(len(long)):
      if long[i] not in short:
        # using pointers rather than slice and compare is faster for large strings
        if long[0:i] + long[i+1:] != short:
          return False

  return True
