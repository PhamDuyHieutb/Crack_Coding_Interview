class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = max_length = 0
        used_char = {}
        for i in range(len(s)):
            if s[i] in used_char and start <= used_char[s[i]]:
                start = used_char[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used_char[s[i]] = i

        return max_length

    def lengof(self, s):
        start = max_length = 0
        used_char = {}


if __name__ == '__main__':
    s = "tmmzuxt"
    sol = Solution()
    result = sol.lengthOfLongestSubstring(s)
    print(result)
