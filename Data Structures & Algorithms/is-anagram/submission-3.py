class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        counterS = {}
        counterT = {}
        for i in range(len(s)):
            if s[i] in counterS.keys():
                counterS[s[i]] += 1
            else:
                counterS[s[i]] = 1

        for i in range(len(t)):
            if t[i] in counterT.keys():
                counterT[t[i]] += 1
            else:
                counterT[t[i]] = 1
        
        #if len(counterS.keys()) != len(counterT.keys()):
        #    return False
    
        for k,v in counterS.items():
            if k in counterT.keys() and counterT[k] == v:
                continue
            return False
        return True

        