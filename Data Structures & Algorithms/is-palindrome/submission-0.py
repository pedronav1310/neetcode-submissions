class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=[]
        for c in s.lower():
            if c.isalnum():
                string.append(c)
        
        left = 0
        right = len(string)-1
        while right >= left:
            if string[left] == string[right]:
                left+=1
                right-=1
            else:
                return False
        return True