# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2


def subarry(nums,k):
    res = 0
    cursum = 0
    prefixsum = {0:1} 


    for n in nums:
        cursum += n
        diff = cursum - k

        res += prefixsum.get(diff,0) 
        prefixsum[cursum] = prefixsum.get(cursum,0) + 1


    return res

