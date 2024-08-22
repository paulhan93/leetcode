# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 
# is written as XII, which is simply X + II. The number 27 is written as XXVII, which 
# is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, 
# the numeral for four is not IIII. Instead, the number four is written as IV. 
# Because the one is before the five we subtract it making four. The same principle 
# applies to the number nine, which is written as IX. There are six instances where 
# subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

# Constraints:
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].


# Solution 1: Larger code, harder to understand
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Create a hash map / dictionry of roman numeral (key) to integer (value) pairs
        map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        # value of the integer as we traverse through the string
        sum = 0

        # find the length of the string 
        s_list = list(enumerate(list(s)))
        s_length = len(s)
        i = 0

        while i <= s_length:
            if i == s_length:
                return sum
            if i == s_length - 1:
                sum+=map[s_list[i][1]]
                return sum
                
            if s_list[i][1] == "C" and s_list[i+1][1] == "M":
                sum+=900
                i+=2
            elif s_list[i][1] == "C" and s_list[i+1][1] == "D":
                sum+=400
                i+=2
            elif s_list[i][1] == "X" and s_list[i+1][1] == "C":
                sum+=90
                i+=2
            elif s_list[i][1] == "X" and s_list[i+1][1] == "L":
                sum+=40
                i+=2
            elif s_list[i][1] == "I" and s_list[i+1][1] == "X":
                sum+=9
                i+=2
            elif s_list[i][1] == "I" and s_list[i+1][1] == "V":
                sum+=4
                i+=2
            else:
                sum+=map[s_list[i][1]]
                i+=1

# Set variable 
s = "MCMXCIV"

# Create an instance of the Solution class
solution = Solution()

# Call the romanToInt method with input s
result = solution.romanToInt(s)
print(result)


# Solution 2: Simpler code, easier to understand
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Create a hash map / dictionry of roman numeral (key) to integer (value) pairs
        map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        # define variables
        total = 0
        prev_value = 0

        # Loop through the string in reverse
        for char in reversed(s):
            current_value = map[char]

            # If the current value is less than the previous value, subtract from the 
            # total. Otherwise, add to the total.
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            
            # Set the previous value to the current value
            prev_value = current_value
        
        return total

# Set variable 
s = "MCMXCIV"

# Create an instance of the Solution class
solution = Solution()

# Call the romanToInt method with input s
result = solution.romanToInt(s)
print(result)
