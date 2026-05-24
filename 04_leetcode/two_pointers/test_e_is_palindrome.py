import unittest
# PyCharm will let you easily auto-import your solution file here later
from coding_file import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_standard_cases(self):
        """Test classic palindrome inputs"""
        # self.assertTrue(self.sol.isPalindrome("A man, a plan, a canal: Panama"))
        pass

    def test_edge_cases(self):
        """Test tricky inputs like empty strings or non-alphanumeric characters"""
        # self.assertTrue(self.sol.isPalindrome(" "))
        pass


if __name__ == "__main__":
    unittest.main()
