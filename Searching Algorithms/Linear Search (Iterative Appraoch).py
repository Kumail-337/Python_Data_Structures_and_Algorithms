def linear_Search(arr,target):
    for count in range(len(arr)):
        if arr[count] == target:
            return True
    return False

print("Enter your list:")
test_list = [int(b) for b in input().split()]
key = int(input("Enter the search element:"))

found = linear_Search(test_list, key)
if found is True:
    print("Value Found")
else:
    print("Value not Found")