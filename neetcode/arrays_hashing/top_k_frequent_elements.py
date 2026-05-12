# Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent
# elements within the array.
# The test cases are generated such that the answer is always unique.
# You may return the output in any order.

# Example 1:
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]

# Example 2:
# Input: nums = [7,7], k = 1
# Output: [7]

# Constraints:
#     1 <= nums.length <= 10^4.
#     -1000 <= nums[i] <= 1000
#     1 <= k <= number of distinct elements in nums.

# from typing import List
#
#
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         freqs = {}
#         for num in nums:
#             if freqs[num]:
#                 freqs[num] += 1
#             else:
#                 freqs[num] = 1
#
#         buckets = [[] * len(nums)]
#         for key in freqs.keys():
#             buckets[freqs[key]].append(key)
#
#         results = []
#         while stop := 0 < k:
#             for bucket in buckets[::-1]:
#                 for val in bucket:
#                     results.append(val)
#                     stop += 1
#
#         return results

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freqs.items():
            buckets[count].append(num)

        result = []

        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
