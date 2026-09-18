# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/

## Hard

class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        start = 0
        end = n-1
        
        while start < end:
            mid = start + (end-start)//2
            
            ## loop break condition
            if (0 < mid) and (nums[mid-1] > nums[mid]):
                return nums[mid]
            
            if nums[mid] > nums[end]:
                start = mid+1
            elif nums[mid] < nums[end]:
                end = mid
            else:
                # nums[mid] == nums[end]
                # → insufficient information
                # → safely discard one duplicate
                end = end-1
        
        return nums[start]