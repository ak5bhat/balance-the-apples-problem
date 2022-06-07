# balance-the-apples-problem
Problem description

A mother has two sons and she has to divide the number of apples from various baskets equally among them. The array contains the list of number of apples in each basket.
The array cannot be rearranged. we have to calculate the sum sequentially. 
Get the array length and apple array list from user and return the array index that acts as the partitioner that divides the apples equally.
Assume the solution exists for every problem.

--------------------------------------------------------------------------------------
Eg1:
len = 5

arr = [1,2,3,4,6]

Output:

3

Output description:

here arr[0]+arr[1]+arr[2] == arr[4]

Return the index that divides the left basket sum and right basket sum
index 3 divides the sum equally so return index 3

---------------------------------------------------------------------------------------
Eg2:

len = 6

arr = [1,2,3,2,3,3]


o/p:

3


o/p description:

arr[0]+arr[1]+arr[2] == arr[4]+arr[5]

return index 3 from the array since it acts as the partitioner in the basket list.

--------------------------------------------------------------------------------------
