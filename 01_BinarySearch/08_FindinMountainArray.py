# https://leetcode.com/problems/find-in-mountain-array/

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        cache = {}

        def get(i):
            if i not in cache:
                cache[i] = mountainArr.get(i)
            return cache[i]

        peak = self.findPeak(get, n)

        idx = self.orderAgnosticBS(get, target, 0, peak, True)
        if idx != -1:
            return idx
        return self.orderAgnosticBS(get, target, peak + 1, n - 1, False)

    def findPeak(self, get, n):
        lo, hi = 0, n - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if get(mid) < get(mid + 1):
                lo = mid + 1
            else:
                hi = mid
        return lo

    def orderAgnosticBS(self, get, target, lo, hi, isAsc):
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            val = get(mid)
            if val == target:
                return mid
            if isAsc:
                if val < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                if val > target:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1