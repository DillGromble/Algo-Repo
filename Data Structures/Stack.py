#------------------------------------------------------------------------------#
# Stack is a linear data structure which follows a particular order in which   #
# the operations are performed. The order may be LIFO(Last In First Out) or    #
# FILO (First In Last Out).                                                    #
# Mainly the following three basic operations are performed in the stack:      #
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# Push:          Adds an item in the stack. If the stack is full,
#                then it's an Overflow condition.
# Pop:           Removes an item from the stack. The items are popped in the
#                reversed order in which they are pushed. If the stack is
#                empty, then it's an Underflow condition.
# Peek or Top:   Returns top element of stack.
# isEmpty:       Returns true if stack is empty, else false.
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
#                        Stack as an Array (List)                              #
#------------------------------------------------------------------------------#

class Stack:

  def __init__(self, size=None):
    self.stack = []
    self.size = size

  def push(self, item):
    if len(self.stack) == self.size:
      raise IndexError('Overflow Error')
    try:
      self.stack.append(item)
    except IndexError:
      print('Overflow Error')

  def pop(self):
    if len(self.stack) == 0:
      raise IndexError('UnderflowError')
    try:
      return self.stack.pop()
    except IndexError:
      print('Underflow Error')

  def peek(self):
    return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0



#------------------------------------------------------------------------------#
#                        Stack as a Linked List                                #
#------------------------------------------------------------------------------#
