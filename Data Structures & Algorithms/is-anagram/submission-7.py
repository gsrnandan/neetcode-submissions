class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        counter = [0] * 26
        
        for i in range(len(s)):
            entry = str(s[i])
            index = ord('a') - ord(entry)
            counter[index] += 1
        
        for i in range(len(t)):
            entry = str(t[i])
            index = ord('a') - ord(entry)
            counter[index] -= 1
            if counter[index] < 0:
                return False
        
        return True
        