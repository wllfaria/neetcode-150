class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset: set[str] = set()
        l = 0
        m = 0

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            m = max(m, r - l + 1)

        return m


print(Solution().lengthOfLongestSubstring("zxyzxyz"))
