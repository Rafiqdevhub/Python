# Task 32: Write a Python program to find the sum of all elements in an array.
nums=[1, 2,3]

res=sum(nums) 
print(res)  # Print the result


def sum_of_array(arr):
    total = 0 
    for element in arr:
        total += element
    return total

array = [1, 2, 3]
result = sum_of_array(array)
# print("Sum of the array:", result)



# Task 33: Write a Python program to find the largest element in an array.
def find_largest_element(arr):
    if not arr:
        return "Array is empty"
    largest_element = arr[0]
    for element in arr:
        if element > largest_element:
            largest_element = element
    return largest_element

my_array = [12, 22,12, 4, 5, 6, 7, 8, 9]
result = find_largest_element(my_array)
print(f"Largest number in the array is: {result}")  # Print the result


# Task 34: Write a Python program to find the smallest element in an array.
def rotate_array(arr, d):
    n = len(arr)
    if d < 0 or d >= n:
        return "Invalid rotation value"
    rotated_arr = [0] * n
    for i in range(n):
        rotated_arr[i] = arr[(i + d) % n]
    return rotated_arr

arr = [1, 2, 3, 4, 15]
d = 2
result = rotate_array(arr, d)
# Print the rotated array
# print("Original Array:", arr)
# print("Rotated Array:", result)



# Task 35: Write a Python program to find the second largest element in an array.
def split_and_add(arr, k):
    if k <= 0 or k >= len(arr):
        return arr  
    first_part = arr[:k]
    second_part = arr[k:]
    result = second_part + first_part
    return result

arr = [1, 2, 3, 4, 5]
k = 3
result = split_and_add(arr, k)
print("Original Array:", arr)
print("Array after splitting and adding:", result)