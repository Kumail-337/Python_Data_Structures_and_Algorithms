def partition(arr,low,high):
    pivot = arr[low]
    x = low
    y = high

    while x < y:
        while arr[x] <= pivot and x <= high - 1:
            x += 1
        while arr[y] > pivot and y >= low + 1:
            y -= 1
        if x < y:
            arr[x],arr[y] = arr[y],arr[x]

    arr[low],arr[y] = arr[y],arr[low]
    return y

def quick_Sort(arr,low,high):
    if low < high:
        p_index = partition(arr,low,high)
        quick_Sort(arr,low,p_index - 1)
        quick_Sort(arr,p_index + 1,high)

nums = [3,1,2,4,7,6,8]
print("\t\t Quick Sort in Ascending Order")
print(f"Before Sorting: {nums}")
quick_Sort(nums,0,len(nums) - 1)
print(f"After Sorting: {nums}")

####################### Quick Sort in Descending Order ##########################
def partition(arr,low,high):
    pivot = arr[low]
    x = low
    y = high

    while x < y:
        while arr[x] >= pivot and x <= high - 1:
            x += 1
        while arr[y] < pivot and y >= low + 1:
            y -= 1
        if x < y:
            arr[x],arr[y] = arr[y],arr[x]

    arr[low],arr[y] = arr[y],arr[low]
    return y

def quick_Sort_Descending(arr,low,high):
    if low < high:
        p_index = partition(arr,low,high)
        quick_Sort_Descending(arr, low, p_index - 1)
        quick_Sort_Descending(arr, p_index + 1, high)

nums = [21,11,5,78,49,54,72,88]
print("\n\t\t Quick Sort in Descending Order")
print(f"Before Sorting: {nums}")
quick_Sort_Descending(nums,0,len(nums) - 1)
print(f"After Sorting: {nums}")