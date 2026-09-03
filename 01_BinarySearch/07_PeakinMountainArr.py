class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        start = 0
        end = len(arr) - 1
        
        while start < end:
            mid = start + (end - start) // 2
            
            # If the next element is smaller, we are on the descending slope.
            # The peak could be at 'mid' or to its left.
            if arr[mid] > arr[mid + 1]:
                end = mid
            else:
                # If the next element is larger, we are on the ascending slope.
                # The peak must be to the right of 'mid'.
                start = mid + 1
                
        # When start == end, it will point exactly to the peak index.
        return start
