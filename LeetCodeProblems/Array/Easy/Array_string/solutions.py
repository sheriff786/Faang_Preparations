"""
========================================
LeetCode Core Array & Permutation Patterns
Author: Your Name
========================================
"""


from typing import List


# ============================================================
"""
Problem: Two Sum
Pattern: Hash Map (Complement Lookup)

Idea:
- Traverse array once
- For each element, check if (target - element) exists
- Store visited elements in hashmap

Time Complexity: O(n)
Space Complexity: O(n)
"""
def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i


# ============================================================
"""
Problem: Longest Common Prefix
Pattern: Vertical Scanning

Idea:
- Take first string as reference
- Compare characters column-wise
- Stop at first mismatch

Time Complexity: O(n * m)
Space Complexity: O(1)
"""
def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""

    first = strs[0]

    for i in range(len(first)):
        for word in strs:
            if i >= len(word) or word[i] != first[i]:
                return first[:i]

    return first


# ============================================================
"""
Problem: 3Sum
Pattern: Sorting + Two Pointers

Idea:
- Sort array
- Fix one element
- Use two pointers to find remaining pair
- Skip duplicates

Time Complexity: O(n^2)
Space Complexity: O(1)
"""
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return res


# ============================================================
"""
Problem: 3Sum Closest
Pattern: Sorting + Two Pointers

Idea:
- Sort array
- Fix one element
- Use two pointers
- Track closest sum using absolute difference

Time Complexity: O(n^2)
Space Complexity: O(1)
"""
def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    closest = nums[0] + nums[1] + nums[2]

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if abs(target - total) < abs(target - closest):
                closest = total

            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return total

    return closest


# ============================================================
"""
Problem: 4Sum
Pattern: Sorting + Two Pointers (k-Sum)

Idea:
- Sort array
- Fix two elements
- Use two pointers
- Skip duplicates

Time Complexity: O(n^3)
Space Complexity: O(1)
"""
def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    res = []

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left, right = j + 1, n - 1

            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total == target:
                    res.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < target:
                    left += 1
                else:
                    right -= 1

    return res


# ============================================================
"""
Problem: Remove Duplicates from Sorted Array
Pattern: Two Pointers (Slow-Fast)

Time Complexity: O(n)
Space Complexity: O(1)
"""
def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0

    slow = 0

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1


# ============================================================
"""
Problem: Remove Element
Pattern: Two Pointers (Overwrite)

Time Complexity: O(n)
Space Complexity: O(1)
"""
def removeElement(nums: List[int], val: int) -> int:
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k


# ============================================================
"""
Problem: Next Permutation
Pattern: Pivot + Reverse Suffix

Steps:
1. Find pivot (first decreasing element from right)
2. If none → reverse entire array
3. Find next greater element to pivot
4. Swap
5. Reverse suffix

Time Complexity: O(n)
Space Complexity: O(1)
"""
def nextPermutation(nums: List[int]) -> None:
    n = len(nums)
    ind = -1

    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            ind = i
            break

    if ind == -1:
        nums.reverse()
        return

    for i in range(n - 1, ind, -1):
        if nums[i] > nums[ind]:
            nums[i], nums[ind] = nums[ind], nums[i]
            break

    nums[ind + 1:] = reversed(nums[ind + 1:])