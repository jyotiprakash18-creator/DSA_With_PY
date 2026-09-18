# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# Medium

class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        start = 0
        end = n-1
        
        while start <= end:
            mid = start + (end-start)//2
            
            ## loop break condition
            if (0 < mid) and (nums[mid-1] > nums[mid]):
                return nums[mid]
            
            if nums[mid] > nums[end]:
                start = mid+1
            else:
                end = mid-1
        
        return nums[0]
            