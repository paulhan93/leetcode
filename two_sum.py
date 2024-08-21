# PROBLEM: 1. Two Sum
#
# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up 
# to target.
#
# You may assume that each input would have exactly one 
# solution, and you may not use the same element twice.
#
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# Optimal Answer
# Time complexity: O(n)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Initialize an empty dictionary to store value-index pairs
        num_map = {}

        # Iterate over the list with both index and value
        for i, num in enumerate(nums):
            complement = target - num  # Calculate the complement

            # If the complement exists in the dictionary, return the indices
            if complement in num_map:
                return [num_map[complement], i]
            
            # If not, add the current number and its index to the dictionary
            num_map[num] = i

# Define variables
nums = [2,7,11,15]
target = 9

# Create an instance of the Solution class
solution = Solution()

# Call the twoSum method with the nums list and target
result = solution.twoSum(nums,target)

print(result)  # Output: [0, 1]



# Non-optimal Answer
# Time complexity: O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if target == nums[i]+nums[j]:
                    return(i,j)

# Define variables
nums = [2,7,11,15]
target = 9

# Create an instance of the Solution class
solution = Solution()

# Call the twoSum method with the nums list and target
result = solution.twoSum(nums,target)

print(result)  # Output: [0, 1]