def recursive_Linear_Search(arr,target,start,end):
    if start < end:
        if arr[start] == target:
            return True
        else:
            return recursive_Linear_Search(arr,target,start + 1,end)
    else:
        return False

print("Enter your list:")
test_list = [int(b) for b in input().split()]
key = int(input("Enter the search element: "))

result = recursive_Linear_Search(test_list, key, 0, len(test_list))

if result:
    print("Found")
else:
    print("Not Found")