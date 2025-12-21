def merge(left,right):
    result = []
    x,y = 0,0
    left_length,right_length = len(left),len(right)

    while x < left_length and y < right_length:
        if left[x] <= right[y]:
            result.append(left[x])
            x += 1
        else:
            result.append(right[y])
            y += 1

    if x < left_length:
        while x < left_length:
            result.append(left[x])
            x += 1
    if y < right_length:
        while y < right_length:
            result.append(right[y])
            y += 1

    return result

def merge_Sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left = merge_Sort(left_arr)
    right = merge_Sort(right_arr)

    return merge(left, right)

nums = [3,1,2,4,1,5,2,6,4]
print("\t\t Merge Sort in Ascending Order")
print(f"Before Sorting: {nums}")
print(f"After Sorting: {merge_Sort(nums)}")

############################## Merge Sort in Descending Order ###########################
def merge_Descending(left,right):
    result = []
    x,y = 0,0
    left_length,right_length = len(left),len(right)

    while x < left_length and y < right_length:
        if left[x] >= right[y]:
            result.append(left[x])
            x += 1
        else:
            result.append(right[y])
            y += 1

    if x < left_length:
        while x < left_length:
            result.append(left[x])
            x += 1
    if y < right_length:
        while y < right_length:
            result.append(right[y])
            y += 1

    return result

def merge_Sort_Descending(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left = merge_Sort_Descending(left_arr)
    right = merge_Sort_Descending(right_arr)

    return merge_Descending(left, right)

nums = [21,11,5,78,49,54,72,88,56,28,10]
print("\n\t\t Merge Sort in Descending Order")
print(f"Before Sorting: {nums}")
print(f"After Sorting: {merge_Sort_Descending(nums)}")