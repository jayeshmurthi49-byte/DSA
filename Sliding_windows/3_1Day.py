def minWindow(s, t):
    if not s or not t:
        return ""                    
    t_count = {}
    for c in t:
        t_count[c] = t_count.get(c, 0) + 1  
    need = len(t_count)
    have = 0
    left = 0
    window = {}
    min_len = float("infinity")
    result = ""
    for right in range(len(s)):
        c = s[right]
        window[c] = window.get(c, 0) + 1    
        if c in t_count and window[c] == t_count[c]:
            have += 1                       
        while have == need:
            if (right - left + 1) < min_len:
                min_len = right - left + 1
                result = s[left:right+1]     
            window[s[left]] -= 1
            if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                have -= 1                   
            left += 1                        
    return result