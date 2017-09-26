import unittest
import Stack


class StackNoneSize(unittest.TestCase):

  def setUp(self):
    self.stack = Stack.Stack()

  def test_is_Stack(self):
    self.assertEqual(self.stack.size, None)
    self.assertIsInstance(self.stack, Stack.Stack)

  def test_push(self):
    self.stack.push(1)
    self.assertEqual(self.stack.stack, [1])
    self.stack.push(2)
    self.assertEqual(self.stack.stack, [1, 2])

  def test_pop(self):
    self.stack.push(1)
    popped = self.stack.pop()
    self.assertEqual(popped, 1)

  def test_underflow(self):
    with self.assertRaises(IndexError) as context:
      self.stack.pop()
    self.assertTrue('Underflow Error' in str(context.exception))

  def test_peek(self):
    self.stack.push(1)
    self.assertEqual(self.stack.peek(), 1)

  def test_isEmpty(self):
    self.assertTrue(self.stack.isEmpty())
    self.stack.push(1)
    self.assertFalse(self.stack.isEmpty())




class StackWithSize(unittest.TestCase):

  def setUp(self):
    self.stack = Stack.Stack(3)

  def test_is_sizedStack(self):
    self.assertEqual(self.stack.size, 3)
    self.assertIsInstance(self.stack, Stack.Stack)

  def test_overflow(self):
    self.stack.push(1)
    self.stack.push(1)
    self.stack.push(1)
    with self.assertRaises(IndexError) as context:
      self.stack.push(1)
    self.assertTrue('Overflow Error' in str(context.exception))




if __name__ == '__main__':
  unittest.main(verbosity=2)
