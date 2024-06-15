Merge List
Write a Python program to Zip two given lists of lists.

Input:
m : row size
n: column size
list1 and list 2 :  Two lists
Output
Zipped List : List which combined both list1 and list2

Sample test case

Sample input
2
2
1 
3
5
7
2
4
6
8

Sample Output

[[1, 3, 2, 4], [5, 7, 6, 8]]

def merge_arrays_without_duplicates(arr1, arr2):
    # Combine the arrays and convert to a set to remove duplicates
    result_set = set(arr1 + arr2)
    # Convert the set back to a sorted list
    merged_sorted_array = sorted(result_set)
    return merged_sorted_array
 
# Input read and processing
def process_input():
    # Reading number of elements and the elements for the first array
    n1 = int(input())
    array1 = []
    for _ in range(n1):
        element = int(input())
        array1.append(element)
 
    # Reading number of elements and the elements for the second array
    n2 = int(input())
    array2 = []
    for _ in range(n2):
        element = int(input())
        array2.append(element)
 
    # Merge the arrays without duplicates
    result = merge_arrays_without_duplicates(array1, array2)
 
    # Print the result
    print(" ".join(map(str, result)))
