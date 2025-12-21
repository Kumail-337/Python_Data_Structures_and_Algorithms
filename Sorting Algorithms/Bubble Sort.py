num_list = [2,43,12,3,1,0,78,4,2,15]

def bubble_Sort(arr):
    a = len(arr)
    b = a - 1
    for x in range(a):
        for y in range(b):
            if arr[y + 1] < arr[y]:
                temp = arr[y + 1]
                arr[y + 1] = arr[y]
                arr[y] = temp

print("\t\t Bubble Sort in Ascending Order")
print(f"Before Sorting: {num_list}")
bubble_Sort(num_list)
print(f"After Sorting: {num_list}")

#################### Bubble Sort in Descending Order #######################
num_list = [3,1,2,4,1,5,2,6,4]

def bubble_Sort_Descending(arr):
    a = len(arr)
    b = a - 1
    for x in range(a):
        for y in range(b):
            if arr[y + 1] > arr[y]:
                arr[y + 1], arr[y] = arr[y], arr[y + 1]

print("\n\t\t Bubble Sort in Descending Order")
print(f"Before Sorting: {num_list}")
bubble_Sort_Descending(num_list)
print(f"After Sorting: {num_list}")