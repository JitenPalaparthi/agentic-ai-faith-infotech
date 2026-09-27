def binary_search(items, target):
    lo, hi = 0, len(items)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if items[mid] == target: return mid
        if items[mid] < target: lo = mid+1
        else: hi = mid-1
    return -1

print(binary_search([1,3,5,7,9], 7))
