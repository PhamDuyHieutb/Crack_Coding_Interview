class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        rev = 0
        while x > rev:
            # reverse gradually
            rev = rev * 10 + x % 10
            # remove character gradually from the number
            x = x // 10

        return x == rev or x == rev // 10


s = Solution()
s.isPalindrome(32123)
