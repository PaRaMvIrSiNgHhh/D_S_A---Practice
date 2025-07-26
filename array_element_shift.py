numbers = [3, 2, 1, 5, 2]

# Find the largest number
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i

print("The largest number is:", largest)

# Find the second largest number
second_largest = -1
for i in numbers:
    if i != largest and i > second_largest:
        second_largest = i

print("The second largest number is:", second_largest)


#_______________________output________________________________________________________________#
# The largest number is: 5
# The second largest number is: 3
arr = [1, 1, 2, 2, 2]

# Initialize index of next unique element
i = 0
for j in range(1, len(arr)):
    if arr[j] != arr[i]:
        i += 1
        arr[i] = arr[j]

# Slice the array to keep only unique elements
unique_arr = arr[:i+1]
print("After removing duplicates:", unique_arr)
