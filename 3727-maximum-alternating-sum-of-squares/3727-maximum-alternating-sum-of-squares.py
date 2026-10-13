
class Solution(object):
    def maxAlternatingSum(self, nums):
        n = len(nums)

        # Sorting is faster for smaller arrays
        if n < 15000:
            a = [x * x for x in nums]
            a.sort()
            mid = n // 2
            return sum(a[mid:]) - sum(a[:mid])

        # Counting approach for larger arrays
        freq = [0] * 40001

        for x in nums:
            freq[abs(x)] += 1

        remaining = n // 2
        ans = 0

        for val, count in enumerate(freq):
            if not count:
                continue

            sq = val * val

            if count <= remaining:
                ans -= count * sq
                remaining -= count
            else:
                ans += (count - 2 * remaining) * sq
                remaining = 0

        return ans
