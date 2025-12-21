Data = [1, 3, 4, 5, 6, 8, 9, 10]

def binary_Search(nums,target):
    n = len(nums)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

value = 15
found = binary_Search(Data,value)
if found is True:
    print("Value found")
else:
    print("Value not found")