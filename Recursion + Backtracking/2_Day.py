


# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]



# https://www.youtube.com/watch?v=s7AvT7cGdSo

def Permutation(nums):
    results  = []

    if len(nums) == 1:
        return [nums[:]]
    
    for i in range(len(nums)):
        n = nums.pop(0)
        parms = Permutation(nums) 

        for parm in parms:
            parm.append(n)
        results.extend(parms)
        nums.append(n)

    return results