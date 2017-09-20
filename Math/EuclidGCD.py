#------------------------------------------------------------------------------#
# Find the Greatest Common Divisor (GCD) of two numbers a and b                #
# Time complexity boils to O(log(b)): (the number of digits in b)              #
#
#     @param a : integer                                                       #
#     @param b : integer                                                       #
#     @return an integer                                                       #
#------------------------------------------------------------------------------#



#------------------------------------------------------------------------------#
# Iterative Solution:                                                          #
#------------------------------------------------------------------------------#
def gcd (a, b):
  # Compute a and b as dividend or divisor
  dividend = a if a >= b else b
  divisor = a if a <= b else b

  # For as long as there is a remainder after % operation:
  # Shift dividend <- divisor <- remainder
  while divisor != 0:
    remainder = dividend % divisor
    dividend = divisor
    divisor = remainder

  return dividend



#------------------------------------------------------------------------------#
# Recursive Solution:                                                          #
# (The iterative solution is considered faster)                                #
#------------------------------------------------------------------------------#
def recursiveGCD (a, b):
  if not b: return a
  return recursiveGCD(b, a % b)




