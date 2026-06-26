# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:

# Input: nums = [3,3,3,3,3]
# Output: 3



def duplicates(nums):
    i = 0 

    while i < len(nums):
        correct = nums[i] - 1

        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i] 

        else:
            i += 1


    for i in range(len(nums)):
        if nums[i] != i + 1:
            return nums[i]