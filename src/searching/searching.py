# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start=0, end=None):
    # Your code here
    # Base Case
    if end >= start: 
        mid = (end + start) // 2  
        # Target element is middle element?
        if arr[mid] == target: 
            return mid
        # If target element is smaller than mid element, check left side of the main array
        elif arr[mid] > target: 
            return binary_search(arr, target,start, (mid-1)) 
        # If not? Check right side of main array
        else: 
            return binary_search(arr, target, (mid + 1), end)
    else: 
        # if all else fails
        return -1
  
















