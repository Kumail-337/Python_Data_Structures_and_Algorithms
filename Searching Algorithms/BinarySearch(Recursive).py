Data = [1, 3, 4, 5, 6, 8, 9, 10]

def recursive_Binary_Search(nums,target,low,high):
    if low > high:
        return False
    mid = (low + high) // 2

    if nums[mid] == target:
        return  True
    elif nums[mid] < target:
        return recursive_Binary_Search(nums,target,mid + 1,high)
    else:
        return recursive_Binary_Search(nums,target,low,mid - 1)

value = 5
found = recursive_Binary_Search(Data,value,0,len(Data))
if found is True:
    print("Value found")
else:
    print("Value not found")