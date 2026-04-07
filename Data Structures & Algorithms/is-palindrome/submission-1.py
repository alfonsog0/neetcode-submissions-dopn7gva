class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        if length == 0:
            return True
        
        start = 0
        end = -1

        while start < length and abs(end) <= length:
            while not (s[start].isalnum()):
                start += 1
                if start >= length:
                    break
            
            while not (s[end].isalnum()):
                end -= 1
                if abs(end) > length:
                    break
            
            if start >= length or abs(end) > length:
                break      
            
            if s[start].lower() != s[end].lower():
                return False
            
            start += 1
            end -= 1
        
        #if start != (abs(end) - 1):
        #    return False
        
        return True
