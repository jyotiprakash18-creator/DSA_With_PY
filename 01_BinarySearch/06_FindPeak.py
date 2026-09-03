# https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        start = 0
        end = len(nums) - 1
        
        while start < end:
            mid = start + (end - start) // 2
            
            # If the next element is smaller, we are on the descending slope.
            # The peak could be at 'mid' or to its left.
            if nums[mid] >nums[mid + 1]:
                end = mid
            else:
                # If the next element is larger, we are on the ascending slope.
                # The peak must be to the right of 'mid'.
                start = mid + 1
                
        # When start == end, it will point exactly to the peak index.
        return start
        