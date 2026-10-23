class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        maximo = 0
        for r in range(len(s)):
            # shrink window from the left until s[r] is no longer a duplicate
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maximo = max(maximo, r - l + 1)
        return maximo