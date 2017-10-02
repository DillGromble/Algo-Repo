import unittest
import longestSubstringNoCharRepeat


class lsNoCharRepeat(unittest.TestCase):

  def setUp(self):
    self.lsNCR = longestSubstringNoCharRepeat.lengthOfLongestSubstring

  def test_handles_empty(self):
    ans = self.lsNCR('')
    self.assertEqual(ans, 0)

  def test_str_len1(self):
    self.assertEqual(self.lsNCR('a'), 1)

  def test_all_same(self):
    self.assertEqual(self.lsNCR('aaaaaaa'), 1)

  def test_various_cases(self):
    self.assertEqual(self.lsNCR('abcabcbb'), 3)
    self.assertEqual(self.lsNCR('twweckt'), 5)
    self.assertEqual(self.lsNCR('acbcbcba'), 3)


if __name__ == '__main__':
  unittest.main(verbosity=2)
