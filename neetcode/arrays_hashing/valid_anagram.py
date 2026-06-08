# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
#
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
#
# Example 1:
#
# Input: s = "racecar", t = "carrace"
#
# Output: true
#
# Example 2:
#
# Input: s = "jar", t = "jam"
#
# Output: false
#
# Constraints:
#
#     1 <= s.length, t.length <= 5 * 10^4
#     s and t consist of lowercase English letters.


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map1 = {}
        map2 = {}

        for letter in s:
            if letter in map1:
                map1[letter] += 1
            else:
                map1[letter] = 1

        for letter in t:
            if letter in map2:
                map2[letter] += 1
            else:
                map2[letter] = 1

        return map1 == map2


sol = Solution()

s, t = "racecar", "carrace"
print(sol.is_anagram(s, t))

s, t = "jar", "jam"
print(sol.is_anagram(s, t))
