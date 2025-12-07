Data = [5,7,8,4,1,6,9,2]

def selection_Sort(nums):
  n = len(nums)
  for i in range(n):
    min_index = i

    for j in range(i+1,n):
      if nums[j] < nums[min_index]:
        min_index = j

    nums[i],nums[min_index] = nums[min_index],nums[i]

print("\t\t Selection Sort in Ascending Order")
print(f"Before Sorting: {Data}")
selection_Sort(Data)
print(f"After Sorting: {Data}")

############################## Selections Sort in Descending Order ################################
Data = [5,7,8,4,1,6,9,2]

def selection_Sort_Descending(nums):
  n = len(nums)
  for i in range(n):
    min_index = i

    for j in range(i+1,n):
      if nums[j] > nums[min_index]:
        min_index = j

    nums[i],nums[min_index] = nums[min_index],nums[i]

print("\n\t\t Selection Sort in Descending Order")
print(f"Before Sorting: {Data}")
selection_Sort_Descending(Data)
print(f"After Sorting: {Data}")