# Group Anagrams
# Medium Topics Company Tags
# Hints
#
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
#
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
#
# Example 1:
#
# Input: strs = ["act","pots","tops","cat","stop","hat"]
#
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
#
# Example 2:
#
# Input: strs = ["x"]
#
# Output: [["x"]]
#
# Example 3:
#
# Input: strs = [""]
#
# Output: [[""]]
#
# Constraints:
#
#     1 <= strs.length <= 1000.
#     0 <= strs[i].length <= 100
#     strs[i] is made up of lowercase English letters.


# Recommended Time & Space Complexity:
# You should aim for a solution with O(m * n) time and O(m) space, where m is the number of strings and n is the length of the longest string.


class Solution:
    def getKeyFromAnagrams(self, anagrams, str):
        for i in range(len(anagrams)):
            if anagrams[i] == str:
                return i

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = [[] * len(strs)]
        map = {}

        for str in strs:
            anagram = [0] * 26
            for l in str:
                idx = ord(l.lower()) - 97
                anagram[idx] += 1
            if not anagram in anagrams:
                anagrams.append(anagram)

            key = self.getKeyFromAnagrams(anagrams, anagram)
            print("key:", key)

            if key in map:
                map[key].append(str)
            else:
                map[key] = [str]

        print(anagrams)
        return list(map.values())


sol = Solution()

strs = ["act", "pots", "tops", "cat", "stop", "hat"]

res = sol.groupAnagrams(strs)
print("res:", res)
if res == [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]:
    print("ok")
else:
    print("no")


# strs = ["x"]
# res = sol.groupAnagrams(strs)
# print(res)
# if res == [["x"]]:
#     print("ok")
#
# strs = [""]
# res = sol.groupAnagrams(strs)
# print(res)
# if res == [[""]]:
#     print("ok")
