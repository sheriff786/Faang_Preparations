'''
Description of the question

You are given an unsorted integer array nums.

You need to find the smallest positive integer that is missing from the array.

For example:

nums = [1, 2, 0]

Positive integers start from:

1, 2, 3, 4, 5, ...

Here 1 and 2 are present, but 3 is missing.

So:

Output = 3

Another example:

nums = [3, 4, -1, 1]

Positive numbers are:

1, 3, 4

1 exists, but 2 is missing.

Output = 2
need solution O(n),spact time O(1)

'''

#solution
#brute force approach sort the array and then find the values ias per index and do return it

#optimize solutions
'''
1.use swapping approach in array of x-1 ---> O(n) and O(1)
2.hash set approach O(n),space O(n)
3.flagging O(n),O(1)

'''
def firstMissingPositive(nums):
    n = len(nums)

    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1

