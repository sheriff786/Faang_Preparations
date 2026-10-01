from typing import List

'''
Sum of All Subsets XOR Total
Easy
Topics
Company Tags
The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
You are given an array nums, return the sum of all XOR totals for every subset of nums.

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

Example 1:

Input: nums = [2,4]

Output: 12
Explanation: The four subsets of [2,4] are

The empty subset has an XOR total of 0.
[2] has an XOR total of 2.
[4] has an XOR total of 4.
[2,4] has an XOR total of (2 XOR 4 = 6).
The sum of all XOR totals is 0 + 2 + 4 + 6 = 12.
Example 2:

Input: [3,1,1]

Output: 12
Explanation: The eight subsets of [3,1,1] are

The empty subset has an XOR total of 0.
[3] has an XOR total of 3.
[1] has an XOR total of 1.
[1] has an XOR total of 1.
[3,1] has an XOR total of (3 XOR 1 = 2).
[3,1] has an XOR total of (3 XOR 1 = 2).
[1,1] has an XOR total of (1 XOR 1 = 0).
[3,1,1] has an XOR total of (3 XOR 1 XOR 1 = 3).
The sum of all XOR totals is 0 + 3 + 1 + 1 + 2 + 2 + 0 + 3 = 12.
Constraints:

1 <= nums.length <= 12
1 <= nums[i] <= 20

'''
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        

        def solve(nums,index,currentxor):
            if index==len(nums):
                return currentxor
            
            #take
            take=solve(nums,index+1,currentxor^nums[index])

            #skip
            skip=solve(nums,index+1,currentxor)

            return skip + take
        return solve(nums,0,0)
        
        
'''
You are given an array of integers candidates, which may contain duplicates, and a target integer target. Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.

Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.

Example 1:

Input: candidates = [9,2,2,4,6,1,5], target = 8

Output: [
  [1,2,5],
  [2,2,4],
  [2,6]
]
Example 2:

Input: candidates = [1,2,3,4,5], target = 7

Output: [
  [1,2,4],
  [2,5],
  [3,4]
]
Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30


'''

'''
DUPLICATES IN BACKTRACKING: CLEAR STEPS AND TRICKS

Step 1: Decide what the answer considers different.
- Subsets/combinations: order does not matter.
  [1, 2] and [2, 1] are the same answer.
- Permutations: order matters.
  [1, 2] and [2, 1] are different answers.

Step 2: Decide whether an index can be reused.
- "Use each element at most once" -> after choosing nums[i], use i + 1.
- "Unlimited reuse" -> after choosing nums[i], use i again.
- Permutations -> use a `used` array; choose any unused index.

Step 3: Sort before backtracking.
Sorting puts equal values together, so one comparison can detect duplicates.

Step 4: Remember the golden rule.
Skip an equal value only when it is another choice at the SAME level.
Do not skip it when it is chosen deeper in the current path.

Example: nums = [1, 1, 2]
At the root, the first 1 explores every answer beginning with 1.
The second 1 would explore the exact same answers, so skip it:
    if i > start and nums[i] == nums[i - 1]:
        continue

But after choosing the first 1, choosing the second 1 is a different depth.
Keep it, because [1, 1] is a valid unique answer.

PATTERN A: SUBSETS II / COMBINATION SUM II
Use a `start` index because order does not matter.

    nums.sort()
    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i - 1]:
            continue                 # duplicate at this level
        path.append(nums[i])
        dfs(i + 1, path)              # each index used once
        path.pop()

PATTERN B: PERMUTATIONS II
Use a `used` array because order matters.

    nums.sort()
    for i in range(len(nums)):
        if used[i]:
            continue
        if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
            continue                 # equal value already had this position
        used[i] = True
        path.append(nums[i])
        dfs(path)
        path.pop()
        used[i] = False

The permutation trick means: use equal values from left to right.
If the previous equal value is still unused, choosing the current one first
would create a duplicate permutation.

PATTERN C: COMBINATION SUM (UNLIMITED REUSE)
There is no same-level duplicate problem in the usual version, but remember:
    dfs(i, path)       # choose nums[i] again
    dfs(i + 1, path)   # skip nums[i]

FINAL 10-SECOND CHECKLIST
1. Sort the input.
2. Is order important? Use `used` for permutations; otherwise use `start`.
3. Is reuse allowed? Choose with `i` or `i + 1` accordingly.
4. For unique subsets/combinations, skip only with `i > start`.
5. For unique permutations, skip equal values when `not used[i - 1]`.
6. Always append, recurse, pop. That is the backtracking cycle.
'''


class DuplicateBacktrackingPatterns:
    """Runnable reference implementations for duplicate-handling problems."""

    def subsets_with_dup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def dfs(start: int, path: List[int]) -> None:
            result.append(path.copy())

            for index in range(start, len(nums)):
                if index > start and nums[index] == nums[index - 1]:
                    continue
                path.append(nums[index])
                dfs(index + 1, path)
                path.pop()

        dfs(0, [])
        return result

    def combination_sum_2(
        self,
        candidates: List[int],
        target: int
    ) -> List[List[int]]:
        candidates.sort()
        result = []

        def dfs(start: int, remaining: int, path: List[int]) -> None:
            if remaining == 0:
                result.append(path.copy())
                return

            for index in range(start, len(candidates)):
                if index > start and candidates[index] == candidates[index - 1]:
                    continue
                if candidates[index] > remaining:
                    break

                path.append(candidates[index])
                dfs(index + 1, remaining - candidates[index], path)
                path.pop()

        dfs(0, target, [])
        return result

    def permute_unique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        used = [False] * len(nums)

        def dfs(path: List[int]) -> None:
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for index in range(len(nums)):
                if used[index]:
                    continue
                if index > 0 and nums[index] == nums[index - 1] \
                        and not used[index - 1]:
                    continue

                used[index] = True
                path.append(nums[index])
                dfs(path)
                path.pop()
                used[index] = False

        dfs([])
        return result

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        from typing import List


class Solution:
    def combinationSum2(
        self,
        candidates: List[int],
        target: int
    ) -> List[List[int]]:

        result = []

        # Sort so duplicate values are next to each other
        candidates.sort()

        def dfs(i, current, total):

            # Target reached
            if total == target:
                result.append(current.copy())
                return

            # Invalid path
            if total > target or i == len(candidates):
                return

            # --------------------------------
            # TAKE candidates[i]
            # --------------------------------

            current.append(candidates[i])

            dfs(
                i + 1,
                current,
                total + candidates[i]
            )

            # Backtrack
            current.pop()

            # --------------------------------
            # SKIP candidates[i]
            # Skip duplicate values
            # --------------------------------

            while (
                i + 1 < len(candidates)
                and candidates[i] == candidates[i + 1]
            ):
                i += 1

            # SKIP
            dfs(
                i + 1,
                current,
                total
            )

        dfs(0, [], 0)

        return result

'''
Subsets II
Medium
Topics
Company Tags
Hints
You are given an array nums of integers, which may contain duplicates. Return all possible subsets.

The solution must not contain duplicate subsets. You may return the solution in any order.

Example 1:

Input: nums = [1,2,1]

Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]
Example 2:

Input: nums = [7,7]

Output: [[],[7], [7,7]]
Constraints:

1 <= nums.length <= 11
-20 <= nums[i] <= 20

'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res

#iterative solution
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        prev_idx = idx = 0

        for i in range(len(nums)):
            idx = prev_idx if i >= 1 and nums[i] == nums[i - 1] else 0
            prev_idx = len(res)
            for j in range(idx, prev_idx):
                tmp = res[j].copy()
                tmp.append(nums[i])
                res.append(tmp)

        return res       


        

