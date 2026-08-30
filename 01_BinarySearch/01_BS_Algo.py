from typing import List
## sorted array
arr = [1,2,5,6,34,45,66,78,99]

# ascending
def bin_search(arr: List[int], target: int) -> int:
    start = 0
    end = len(arr)-1
    
    while start <= end:
        mid = ((end-start)//2)+start
        
        if target == arr[mid]:
            return mid
        
        if (target > arr[mid]):
            start = mid+1 
        else:
            end = mid-1
    
    return -1

print(bin_search("arr", 34))