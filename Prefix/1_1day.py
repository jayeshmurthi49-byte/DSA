# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

# Example 1:

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]


def totalsum(nums):
    prefix = []
    cur = 0

    for n in nums:
        cur += n
        prefix.append(cur)


    return prefix

def rangesum(left,right,prefix):
    rightsum = prefix[right]
    leftsum = prefix[left - 1] if left > 0 else 0
    return rightsum - leftsum

nums = [2, 4, 6, 8]
prefix = totalsum(nums)

print(rangesum(1, 3, prefix)) 