class Solution:
    # https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        return [self.binary_search(nums, target, True), self.binary_search(nums, target, False)]
    
    def binary_search(self, arr: list[int], target: int, isFirstOccurrence: bool) -> int:
        start = 0
        end = len(arr)-1
        ans = -1
        while start<= end:
            mid = ((end-start)//2)+ start

            if arr[mid] == target:
                ans = mid
                if (isFirstOccurrence):
                    end = mid-1
                else:
                    start = mid+1
            elif arr[mid] < target:
                start = mid+1
            else:
                end = mid-1
        return ans

    
if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    sl = Solution()
    print(sl.searchRange(nums, 8))