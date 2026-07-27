def anagram(s,t):
    if len(s) != len(t):
        return False 

    cout = {}

    for c in s:
        cout[c] = cout.get(c,0) + 1 


        for c in t:
            if c not in t:
                return False

            cout[c] -= 1
            if cout[c] < 0 :
                return False

        return True 