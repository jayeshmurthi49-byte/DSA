# Keywords →
# ✅ "sorted array find pair"
# ✅ "1-indexed"
# → Two Pointer!

def twosum(num,target):
    left = 0
    right = len(num) - 1

    while left < right :
        total = num[left] + num[right]

        if total > target:
            right -= 1
        elif total < target:
            left += 1

        else:
            return [left + 1,right + 1]