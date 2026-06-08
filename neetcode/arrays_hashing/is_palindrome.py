class Solution:
    def is_palindrome(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ptr1 = 0
        ptr2 = len(t) - 1

        for _ in range(len(t)):
            if s[ptr1] != t[ptr2]:
                return False
            ptr1 += 1
            ptr2 -= 1

        return True


sol = Solution()


s, t = "racecar", "carrace"
print(sol.is_palindrome(s, t))
s, t = "jar", "jam"
print(sol.is_palindrome(s, t))
