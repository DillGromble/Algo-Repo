import unittest
import oneAway


class oneAwayTest(unittest.TestCase):

  def setUp(self):
    self.oneAway = oneAway.oneAway

  def test_len_gt_1(self):
    self.assertFalse(self.oneAway('abc', 'abcdd'))

  def test_order_of_strings(self):
    self.assertTrue(self.oneAway('abcd', 'abc'))
    self.assertTrue(self.oneAway('abc', 'abcd'))

  def test_len_1_diff(self):
    self.assertFalse(self.oneAway('abcd', 'abe'))
    self.assertTrue(self.oneAway('abcd', 'abc'))
    self.assertTrue(self.oneAway('acd', 'abcd'))

  def test_same_length(self):
    self.assertFalse(self.oneAway('pale', 'bake'))
    self.assertTrue(self.oneAway('pale', 'bale'))



if __name__ == '__main__':
  unittest.main(verbosity=2)
