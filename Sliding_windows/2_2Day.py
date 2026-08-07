# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false 

from collections import Counter

def checkinclusion(s1,s2):
    if len(s1) > len(s2):
        return False 

    s1_count = Counter(s1)
    window = Counter(s2[:len(s1)])

    if s1_count == window:
        return True

    for i in range(len(s1),len(s2)):
        window[s2[i]] += 1
        window[s2[i - len(s1)]] -= 1

        if window[s2[i - len(s1)]] == 0:
            del window[s2[i- len(s1)]]

        if s1_count == window:
            return True

    return False