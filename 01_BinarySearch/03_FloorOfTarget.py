arr = [1,2,10,13,15,23,26,34,45,55,78,99]

def floor_of_target(arr: list[int], target: int) -> int:
    start = 0
    end = len(arr) - 1
    
    if target < arr[start]:
        return -1
    
    while start<=end:
        mid = ((end-start)//2)+start
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid+1
        else:
            end = mid-1
        
    return end

print(floor_of_target(arr, 17))