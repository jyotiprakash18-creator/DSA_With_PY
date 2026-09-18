# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

# Medium

"""
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        
        peak = self.findPeak(nums, start, end)
        
        if target == nums[peak]:
            return peak
        
        if nums[start] <= target < nums[peak]:
            return self.binSearch(nums, target, start, peak-1)
        else:
            return self.binSearch(nums, target, peak+1, end)
    
    def findPeak(self, arr: list[int], start:int, end:int) -> int:
        n = len(arr)
        while start<=end:
            mid = start + (end-start)//2
            
            if (mid < n-1) and arr[mid] > arr[mid+1]:
                return mid
            
            #after mid if start > mid, then after mid all will be smaller than start right.
            if (arr[start] > arr[mid]):
                end = mid-1
            else:
                start = mid+1
        
        return n-1
            
    def binSearch(self, arr: list[int], target: int, start: int, end: int):
        while start<=end:
            mid = start+(end-start)//2
            
            if (target < arr[mid]):
                end = mid-1
            elif(arr[mid] < target):
                start = mid+1
            else:
                return mid
        return -1