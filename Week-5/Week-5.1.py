Balanced Array
Given an array of numbers, find the index of the smallest array element (the pivot), for which the sums of all elements to the left and to the right are equal. The array may not be reordered.
Example
arr=[1,2,3,4,6]
·         the sum of the first three elements, 1+2+3=6. The value of the last element is 6.
·         Using zero based indexing, arr[3]=4 is the pivot between the two subarrays.
·         The index of the pivot is 3.
Constraints
·         3 ≤ n ≤ 105
·         1 ≤ arr[i] ≤ 2 × 104, where 0 ≤ i < n
·         It is guaranteed that a solution always exists.
The first line contains an integer n, the size of the array arr.
Each of the next n lines contains an integer, arr[i], where 0 ≤ i < n.
Sample Case 0
Sample Input 0
4
1
2
3
3
Sample Output 0
2

a=int(input())
l=[]
for i in range(a):
    c=int(input())
    l.append(c)
for i in range(1,a):
    d=sum(l[0:i])
    r=sum(l[i+1:])
    if(d==r):
        print(i)
