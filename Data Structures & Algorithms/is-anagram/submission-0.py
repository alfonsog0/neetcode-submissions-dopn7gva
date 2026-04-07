class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        freq_t = {}

        for e in s:
            if e in freq_s:
                freq_s[e] += 1
            else:
                freq_s[e] = 1
        
        for d in t:
            if d in freq_t:
                freq_t[d] += 1
            else:
                freq_t[d] = 1
        
        return freq_s == freq_t
        
