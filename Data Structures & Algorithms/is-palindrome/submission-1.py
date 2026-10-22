class Solution:
    def isPalindrome(self, s: str) -> bool:
        dup = ''
        l = 0
        r = len(s)-1
        for c in s:
            if c.isalnum():
                dup += c.upper()
        return dup == dup[::-1]
                