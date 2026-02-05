"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/

Pattern:
- Hash Map (Complement lookup)

Idea:
- Traverse array once
- For each number, check if (target - num) exists
- Store numbers in hashmap with index

Why not two pointers?
- Array is NOT sorted

Time Complexity: O(n)
Space Complexity: O(n)

Edge Cases:
- Duplicate numbers
- Same number cannot be used twice
"""

def twoSum(nums, target):
    seen={}

    for i in range(0,len(nums)):
        diff=target-nums[i]

        if diff in seen:
            return [seen[diff],i]
        seen[nums[i]]=i
