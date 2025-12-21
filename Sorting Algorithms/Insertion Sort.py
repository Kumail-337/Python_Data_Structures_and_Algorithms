nums = [3, 5, 6, 4, 8, 9, 10, 1]

def insertion_Sort(arr):
    n = len(arr)
    for x in range(1, n):
        key = arr[x]
        y = x - 1

        while y >= 0 and arr[y] > key:
            arr[y + 1] = arr[y]
            y -= 1
        arr[y + 1] = key

print("\t\t Insertion Sort in Ascending Order")
print(f"Before Sorting: {nums}")
insertion_Sort(nums)
print(f"After Sorting: {nums}")

#############  Procedure of This Sorting Algorithm  #############
# We assume first element is already sorted
# Key used for storing any element if it's in a wrong position
# Y is used for Comparing the element before x with the current element of x
# The while Loop will run until y's values becomes -1 and the previous index element is greater than next index element
# Within while loop we Copy the greater value and shift it to its right index
# Decrement Y to move to the previous element to continue comparison
# Insert the 'key' at its correct position in the sorted portion

###################### Insertion Sort in Descending Order #######################
nums = [21,11,5,78,49,54,72,88]

def insertion_Sort_Descending(arr):
    n = len(arr)
    for x in range(1, n):
        key = arr[x]
        y = x - 1

        while y >= 0 and arr[y] < key:
            arr[y + 1] = arr[y]
            y -= 1
        arr[y + 1] = key

print("\n\t\t Insertion Sort in Descending Order")
print(f"Before Sorting: {nums}")
insertion_Sort_Descending(nums)
print(f"After Sorting: {nums}")