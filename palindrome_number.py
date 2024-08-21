# Given an integer x, return true if x is a palindrome, and 
# false otherwise.

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Constraints:
# -231 <= x <= 231 - 1

# Answer
# Converting integer to string
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # convert x to string
        num = str(x)

        # set a variable reversing the string
        num_reverse = num[::-1]

        # check if they match; if so it is palindrome
        if num == num_reverse:
            return True
        return False

# Define variable
x = 121

# Create an instance of the Solution class
solution = Solution()

# Call the isPalindrome method with x
result = solution.isPalindrome(x)

print(result)