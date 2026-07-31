#printall subset sum


arr=[1,2,3]
i=0
ans=[]

def printSubsetSum(arr,index,current):
    if index == len(arr):
        print(current)
        return
    
    #incude step
    current.append(arr[index])
    printSubsetSum(arr,index+1,current)
    
    current.pop()
    
    #exclude step
    printSubsetSum(arr,index+1,current)

printSubsetSum(arr,i,ans)
'''

printSubsetSum([1,2,3], 0, [])
├── INCLUDE 1 → current=[1]
│   ├── printSubsetSum([1,2,3], 1, [1])
│   │   ├── INCLUDE 2 → current=[1,2]
│   │   │   ├── printSubsetSum([1,2,3], 2, [1,2])
│   │   │   │   ├── INCLUDE 3 → current=[1,2,3]
│   │   │   │   │   ├── printSubsetSum([1,2,3], 3, [1,2,3])
│   │   │   │   │   │   └── ✅ PRINT [1,2,3] (base case: index==len)
│   │   │   │   │   └── return
│   │   │   │   ├── pop() → current=[1,2]
│   │   │   │   ├── EXCLUDE 3
│   │   │   │   │   ├── printSubsetSum([1,2,3], 3, [1,2])
│   │   │   │   │   │   └── ✅ PRINT [1,2]
│   │   │   │   │   └── return
│   │   ├── pop() → current=[1]
│   │   ├── EXCLUDE 2
│   │   │   ├── printSubsetSum([1,2,3], 2, [1])
│   │   │   │   ├── INCLUDE 3 → current=[1,3]
│   │   │   │   │   ├── printSubsetSum([1,2,3], 3, [1,3])
│   │   │   │   │   │   └── ✅ PRINT [1,3]
│   │   │   │   │   └── return
│   │   │   │   ├── pop() → current=[1]
│   │   │   │   ├── EXCLUDE 3
│   │   │   │   │   ├── printSubsetSum([1,2,3], 3, [1])
│   │   │   │   │   │   └── ✅ PRINT [1]
│   │   │   │   │   └── return
├── pop() → current=[]
├── EXCLUDE 1
│   ├── printSubsetSum([1,2,3], 1, [])
│   │   ├── INCLUDE 2 → current=[2]
│   │   │   ├── printSubsetSum([1,2,3], 2, [2])
│   │   │   │   ├── INCLUDE 3 → current=[2,3]
│   │   │   │   │   ├── printSubsetSum([1,2,3], 3, [2,3])
│   │   │   │   │   │   └── ✅ PRINT [2,3]
│   │   │   │   │   └── return
│   │   │   │   ├── pop() → current=[2]
│   │   │   │   ├── EXCLUDE 3
│   │   │   │   │   ├── printSubsetSum([1,2,3], 3, [2])
│   │   │   │   │   │   └── ✅ PRINT [2]
│   │   │   │   │   └── return
│   │   ├── pop() → current=[]
│   │   ├── EXCLUDE 2
│   │   │   ├── printSubsetSum([1,2,3], 2, [])
│   │   │   │   ├── INCLUDE 3 → current=[3]
│   │   │   │   │   ├── printSubsetSum([1,2,3], 3, [3])
│   │   │   │   │   │   └── ✅ PRINT [3]
│   │   │   │   │   └── return
│   │   │   │   ├── pop() → current=[]
│   │   │   │   ├── EXCLUDE 3
│   │   │   │   │   ├── printSubsetSum([1,2,3], 3, [])
│   │   │   │   │   │   └── ✅ PRINT []
│   │   │   │   │   └── return
'''


#printing subsequence as per target

arr=[1,2,1]
i=0
ans=[]
target=3

print("\n targetSubsets")
def targetSubsequence(arr,index,current,target):
    
    if index==len(arr):
        if sum(current)==target:
            print(current)
            return
        return
    current.append(arr[index])
    targetSubsequence(arr,index+1,current,target)
    current.pop()
    targetSubsequence(arr,index+1,current,target)
    
targetSubsequence(arr,i,ans,target)

#count target subsequences
print("\n countTargetSubsequences")
def countTargetSubsequence(arr,index,current,target):
    if index==len(arr):
        if sum(current)==target:
            return 1
        return 0
    current.append(arr[index])
    left=countTargetSubsequence(arr,index+1,current,target)
    current.pop()
    right=countTargetSubsequence(arr,index+1,current,target)
    return left+right

print(countTargetSubsequence(arr,i,ans,target))



print("\n combination sum 1")

def solve(arr, i, target, current, result, visited):

    # Base Case
    if i == len(arr) or target < 0:
        return

    if target == 0:
        t = tuple(current)
        if t not in visited:
            visited.add(t)
            result.append(current[:])
        return

    # Include
    current.append(arr[i])

    # Single
    solve(arr, i + 1, target - arr[i], current, result, visited)

    # Multiple
    solve(arr, i, target - arr[i], current, result, visited)

    # Backtrack
    current.pop()

    # Exclude
    solve(arr, i + 1, target, current, result, visited)


def combination_sum(arr, target):
    result = []
    visited = set()

    solve(arr, 0, target, [], result, visited)

    return result


# Driver
arr = [2, 3, 6, 7]
target = 7

print(combination_sum(arr, target))

'''
combination_sum([2,3,6,7], 7)
└── solve(i=0, target=7, current=[])
    ├── INCLUDE 2 → current=[2]
    │   ├── SINGLE: solve(i=1, target=5, current=[2])
    │   │   ├── INCLUDE 3 → current=[2,3]
    │   │   │   ├── SINGLE: solve(i=2, target=2, current=[2,3])
    │   │   │   │   ├── INCLUDE 6 → current=[2,3,6]
    │   │   │   │   │   ├── SINGLE: solve(i=3, target=-4) → return (target<0)
    │   │   │   │   │   └── MULTIPLE: solve(i=2, target=-4) → return (target<0)
    │   │   │   │   ├── BACKTRACK → current=[2,3]
    │   │   │   │   └── EXCLUDE: solve(i=3, target=2, current=[2,3])
    │   │   │   │       ├── INCLUDE 7 → current=[2,3,7]
    │   │   │   │       │   ├── SINGLE: solve(i=4) → return (i==len)
    │   │   │   │       │   └── MULTIPLE: solve(i=3, target=-5) → return (target<0)
    │   │   │   │       ├── BACKTRACK → current=[2,3]
    │   │   │   │       └── EXCLUDE: solve(i=4) → return (i==len)
    │   │   │   ├── MULTIPLE: solve(i=1, target=2, current=[2,3])
    │   │   │   │   ├── INCLUDE 3 → current=[2,3,3]
    │   │   │   │   │   ├── SINGLE: solve(i=2, target=-1) → return (target<0)
    │   │   │   │   │   └── MULTIPLE: solve(i=1, target=-1) → return (target<0)
    │   │   │   │   ├── BACKTRACK → current=[2,3]
    │   │   │   │   └── EXCLUDE: solve(i=2, target=2, current=[2,3])
    │   │   │   │       ├── INCLUDE 6 → target=-4 → return (target<0)
    │   │   │   │       ├── BACKTRACK → current=[2,3]
    │   │   │   │       └── EXCLUDE: solve(i=3, target=2, current=[2,3])
    │   │   │   │           ├── INCLUDE 7 → target=-5 → return
    │   │   │   │           ├── BACKTRACK → current=[2,3]
    │   │   │   │           └── EXCLUDE: solve(i=4) → return (i==len)
    │   │   │   ├── BACKTRACK → current=[2]
    │   │   │   └── EXCLUDE: solve(i=2, target=5, current=[2])
    │   │   │       ├── INCLUDE 6 → current=[2,6]
    │   │   │       │   ├── SINGLE: solve(i=3, target=-1) → return (target<0)
    │   │   │       │   └── MULTIPLE: solve(i=2, target=-1) → return (target<0)
    │   │   │       ├── BACKTRACK → current=[2]
    │   │   │       └── EXCLUDE: solve(i=3, target=5, current=[2])
    │   │   │           ├── INCLUDE 7 → current=[2,7], target=-2 → return
    │   │   │           ├── BACKTRACK → current=[2]
    │   │   │           └── EXCLUDE: solve(i=4) → return (i==len)
    │   │
    │   ├── MULTIPLE: solve(i=0, target=5, current=[2])
    │   │   ├── INCLUDE 2 → current=[2,2]
    │   │   │   ├── SINGLE: solve(i=1, target=3, current=[2,2])
    │   │   │   │   ├── INCLUDE 3 → current=[2,2,3]
    │   │   │   │   │   ├── SINGLE: solve(i=2, target=0, current=[2,2,3])
    │   │   │   │   │   │   └── ✅ target==0! result.append([2,2,3])
    │   │   │   │   │   └── MULTIPLE: solve(i=1, target=0, current=[2,2,3])
    │   │   │   │   │       └── target==0, (2,2,3) already visited → return
    │   │   │   │   ├── BACKTRACK → current=[2,2]
    │   │   │   │   └── EXCLUDE: solve(i=2, target=3, current=[2,2])
    │   │   │   │       ├── INCLUDE 6 → target=-3 → return (target<0)
    │   │   │   │       ├── BACKTRACK → current=[2,2]
    │   │   │   │       └── EXCLUDE: solve(i=3, target=3, current=[2,2])
    │   │   │   │           ├── INCLUDE 7 → target=-4 → return
    │   │   │   │           ├── BACKTRACK → current=[2,2]
    │   │   │   │           └── EXCLUDE: solve(i=4) → return (i==len)
    │   │   │   ├── MULTIPLE: solve(i=0, target=3, current=[2,2])
    │   │   │   │   ├── INCLUDE 2 → current=[2,2,2]
    │   │   │   │   │   ├── SINGLE: solve(i=1, target=1, current=[2,2,2])
    │   │   │   │   │   │   ├── INCLUDE 3 → target=-2 → return
    │   │   │   │   │   │   ├── BACKTRACK → current=[2,2,2]
    │   │   │   │   │   │   └── EXCLUDE: solve(i=2, target=1)
    │   │   │   │   │   │       ├── INCLUDE 6 → target=-5 → return
    │   │   │   │   │   │       ├── BACKTRACK → current=[2,2,2]
    │   │   │   │   │   │       └── EXCLUDE: solve(i=3, target=1)
    │   │   │   │   │   │           ├── INCLUDE 7 → target=-6 → return
    │   │   │   │   │   │           ├── BACKTRACK → current=[2,2,2]
    │   │   │   │   │   │           └── EXCLUDE: solve(i=4) → return (i==len)
    │   │   │   │   │   ├── MULTIPLE: solve(i=0, target=1, current=[2,2,2])
    │   │   │   │   │   │   ├── INCLUDE 2 → target=-1 → return (target<0)
    │   │   │   │   │   │   ├── BACKTRACK → current=[2,2,2]
    │   │   │   │   │   │   └── EXCLUDE: solve(i=1, target=1, current=[2,2,2])
    │   │   │   │   │   │       ├── INCLUDE 3 → target=-2 → return
    │   │   │   │   │   │       ├── BACKTRACK → current=[2,2,2]
    │   │   │   │   │   │       └── EXCLUDE: solve(i=2, target=1) → (all fail)
    │   │   │   │   │   ├── BACKTRACK → current=[2,2]
    │   │   │   │   │   └── ...remaining paths pruned (target<0 or i==len)
    │   │   │   │   ├── BACKTRACK → current=[2,2]
    │   │   │   │   └── EXCLUDE: solve(i=1, target=3, current=[2,2])
    │   │   │   │       └── (finds [2,2,3] again → already visited, skipped)
    │   │   ├── BACKTRACK → current=[2]
    │   │   └── EXCLUDE: solve(i=1, target=5, current=[2])
    │   │       ├── INCLUDE 3 → current=[2,3]
    │   │       │   └── ...all paths fail (target<0 or i==len)
    │   │       ├── BACKTRACK → current=[2]
    │   │       └── EXCLUDE: solve(i=2, target=5, current=[2])
    │   │           └── ...all paths fail
    │   │
    ├── BACKTRACK → current=[]
    │
    └── EXCLUDE: solve(i=1, target=7, current=[])
        ├── INCLUDE 3 → current=[3]
        │   ├── SINGLE: solve(i=2, target=4, current=[3])
        │   │   ├── INCLUDE 6 → target=-2 → return (target<0)
        │   │   ├── BACKTRACK → current=[3]
        │   │   └── EXCLUDE: solve(i=3, target=4, current=[3])
        │   │       ├── INCLUDE 7 → target=-3 → return
        │   │       ├── BACKTRACK → current=[3]
        │   │       └── EXCLUDE: solve(i=4) → return (i==len)
        │   ├── MULTIPLE: solve(i=1, target=4, current=[3])
        │   │   ├── INCLUDE 3 → current=[3,3]
        │   │   │   ├── SINGLE: solve(i=2, target=1) → all fail
        │   │   │   ├── MULTIPLE: solve(i=1, target=1) → all fail
        │   │   │   ├── BACKTRACK → current=[3]
        │   │   │   └── EXCLUDE: solve(i=2, target=4)
        │   │   │       ├── INCLUDE 6 → target=-2 → return
        │   │   │       ├── BACKTRACK → current=[3]
        │   │   │       └── EXCLUDE: solve(i=3, target=4)
        │   │   │           ├── INCLUDE 7 → target=-3 → return
        │   │   │           ├── BACKTRACK → current=[3]
        │   │   │           └── EXCLUDE: solve(i=4) → return (i==len)
        │   │   ├── BACKTRACK → current=[3]
        │   │   └── ...remaining pruned
        │   ├── BACKTRACK → current=[]
        │   └── EXCLUDE: solve(i=2, target=7, current=[])
        │       ├── INCLUDE 6 → current=[6]
        │       │   ├── SINGLE: solve(i=3, target=1, current=[6])
        │       │   │   ├── INCLUDE 7 → target=-6 → return
        │       │   │   ├── BACKTRACK → current=[6]
        │       │   │   └── EXCLUDE: solve(i=4) → return (i==len)
        │       │   ├── MULTIPLE: solve(i=2, target=1, current=[6])
        │       │   │   ├── INCLUDE 6 → target=-5 → return
        │       │   │   ├── BACKTRACK → current=[6]
        │       │   │   └── EXCLUDE: solve(i=3, target=1) → all fail
        │       │   ├── BACKTRACK → current=[]
        │       │   └── EXCLUDE: solve(i=3, target=7, current=[])
        │       │       ├── INCLUDE 7 → current=[7]
        │       │       │   ├── SINGLE: solve(i=4, target=0, current=[7])
        │       │       │   │   └── i==len(arr) → return (misses target==0!)
        │       │       │   ├── MULTIPLE: solve(i=3, target=0, current=[7])
        │       │       │   │   └── ✅ target==0! result.append([7])
        │       │       │   ├── BACKTRACK → current=[]
        │       │       │   └── EXCLUDE: solve(i=4) → return (i==len)
        │       │       ├── BACKTRACK → current=[]
        │       │       └── EXCLUDE: solve(i=4) → return (i==len)

SOLUTIONS FOUND:
─────────────────
Path 1: i=0 INCLUDE → MULTIPLE → i=0 INCLUDE → SINGLE → i=1 INCLUDE → SINGLE
         → ✅ [2, 2, 3]

Path 2: i=0 EXCLUDE → i=1 EXCLUDE → i=2 EXCLUDE → i=3 INCLUDE → MULTIPLE
         → ✅ [7]

Final Output: [[2, 2, 3], [7]]

NOTE: The "SINGLE" branch = use element once, move to i+1
      The "MULTIPLE" branch = use element again, stay at i
      The "EXCLUDE" branch = skip element, move to i+1
      Bug: if i==len AND target==0, the i==len check returns FIRST (misses solution)
           That's why [7] is found via MULTIPLE(i=3) not SINGLE(i=4)
'''


'''
recursion call stack 

combination_sum([2,3,6,7], 7)
└── solve(arr, i=0, target=7, current=[], ...)

solve(i=0, target=7, current=[])
├── INCLUDE 2 → current=[2]
│   ├── SINGLE: solve(i=1, target=5, current=[2])
│   │   ├── INCLUDE 3 → current=[2,3]
│   │   │   ├── SINGLE: solve(i=2, target=2, current=[2,3])
│   │   │   │   ├── INCLUDE 6 → current=[2,3,6]
│   │   │   │   │   ├── SINGLE: solve(i=3, target=-4) → return (target<0)
│   │   │   │   │   └── MULTIPLE: solve(i=2, target=-4) → return (target<0)
│   │   │   │   ├── BACKTRACK → current=[2,3]
│   │   │   │   └── EXCLUDE: solve(i=3, target=2, current=[2,3])
│   │   │   │       ├── INCLUDE 7 → current=[2,3,7]
│   │   │   │       │   ├── SINGLE: solve(i=4, target=-5) → return (i==len)
│   │   │   │       │   └── MULTIPLE: solve(i=3, target=-5) → return (target<0)
│   │   │   │       ├── BACKTRACK → current=[2,3]
│   │   │   │       └── EXCLUDE: solve(i=4, target=2) → return (i==len)
│   │   │   ├── MULTIPLE: solve(i=1, target=2, current=[2,3])
│   │   │   │   ├── INCLUDE 3 → current=[2,3,3]
│   │   │   │   │   ├── SINGLE: solve(i=2, target=-1) → return (target<0)
│   │   │   │   │   └── MULTIPLE: solve(i=1, target=-1) → return (target<0)
│   │   │   │   ├── BACKTRACK → current=[2,3]
│   │   │   │   └── EXCLUDE: solve(i=2, target=2, current=[2,3])
│   │   │   │       ├── INCLUDE 6 → current=[2,3,6]
│   │   │   │       │   ├── SINGLE: solve(i=3, target=-4) → return (target<0)
│   │   │   │       │   └── MULTIPLE: solve(i=2, target=-4) → return (target<0)
│   │   │   │       ├── BACKTRACK → current=[2,3]
│   │   │   │       └── EXCLUDE: solve(i=3, target=2, current=[2,3])
│   │   │   │           ├── INCLUDE 7 → [2,3,7], target=-5 → return
│   │   │   │           ├── BACKTRACK → current=[2,3]
│   │   │   │           └── EXCLUDE: solve(i=4) → return (i==len)
│   │   │   ├── BACKTRACK → current=[2]
│   │   │   └── EXCLUDE: solve(i=2, target=5, current=[2])
│   │   │       ├── INCLUDE 6 → current=[2,6]
│   │   │       │   ├── SINGLE: solve(i=3, target=-1) → return (target<0)
│   │   │       │   └── MULTIPLE: solve(i=2, target=-1) → return (target<0)
│   │   │       ├── BACKTRACK → current=[2]
│   │   │       └── EXCLUDE: solve(i=3, target=5, current=[2])
│   │   │           ├── INCLUDE 7 → current=[2,7]
│   │   │           │   ├── SINGLE: solve(i=4, target=-2) → return (i==len)
│   │   │           │   └── MULTIPLE: solve(i=3, target=-2) → return (target<0)
│   │   │           ├── BACKTRACK → current=[2]
│   │   │           └── EXCLUDE: solve(i=4, target=5) → return (i==len)
│   │
│   ├── MULTIPLE: solve(i=0, target=5, current=[2])
│   │   ├── INCLUDE 2 → current=[2,2]
│   │   │   ├── SINGLE: solve(i=1, target=3, current=[2,2])
│   │   │   │   ├── INCLUDE 3 → current=[2,2,3]
│   │   │   │   │   ├── SINGLE: solve(i=2, target=0, current=[2,2,3])
│   │   │   │   │   │   └── ✅ target==0! → result.append([2,2,3])
│   │   │   │   │   └── MULTIPLE: solve(i=1, target=0, current=[2,2,3])
│   │   │   │   │       └── ✅ target==0, but (2,2,3) already visited → return
│   │   │   │   ├── BACKTRACK → current=[2,2]
│   │   │   │   └── EXCLUDE: solve(i=2, target=3, current=[2,2])
│   │   │   │       ├── INCLUDE 6 → current=[2,2,6]
│   │   │   │       │   ├── SINGLE: solve(i=3, target=-3) → return (target<0)
│   │   │   │       │   └── MULTIPLE: solve(i=2, target=-3) → return (target<0)
│   │   │   │       ├── BACKTRACK → current=[2,2]
│   │   │   │       └── EXCLUDE: solve(i=3, target=3, current=[2,2])
│   │   │   │           ├── INCLUDE 7 → current=[2,2,7]
│   │   │   │           │   ├── SINGLE: solve(i=4, target=-4) → return (i==len)
│   │   │   │           │   └── MULTIPLE: solve(i=3, target=-4) → return (target<0)
│   │   │   │           ├── BACKTRACK → current=[2,2]
│   │   │   │           └── EXCLUDE: solve(i=4, target=3) → return (i==len)
│   │   │   ├── MULTIPLE: solve(i=0, target=3, current=[2,2])
│   │   │   │   ├── INCLUDE 2 → current=[2,2,2]
│   │   │   │   │   ├── SINGLE: solve(i=1, target=1, current=[2,2,2])
│   │   │   │   │   │   ├── INCLUDE 3 → [2,2,2,3], target=-2 → return
│   │   │   │   │   │   ├── BACKTRACK → current=[2,2,2]
│   │   │   │   │   │   └── EXCLUDE: solve(i=2, target=1, current=[2,2,2])
│   │   │   │   │   │       ├── INCLUDE 6 → target=-5 → return
│   │   │   │   │   │       ├── BACKTRACK → current=[2,2,2]
│   │   │   │   │   │       └── EXCLUDE: solve(i=3, target=1, current=[2,2,2])
│   │   │   │   │   │           ├── INCLUDE 7 → target=-6 → return
│   │   │   │   │   │           ├── BACKTRACK → current=[2,2,2]
│   │   │   │   │   │           └── EXCLUDE: solve(i=4) → return (i==len)
│   │   │   │   │   ├── MULTIPLE: solve(i=0, target=1, current=[2,2,2])
│   │   │   │   │   │   ├── INCLUDE 2 → [2,2,2,2], target=-1 → return
│   │   │   │   │   │   ├── BACKTRACK → current=[2,2,2]
│   │   │   │   │   │   └── EXCLUDE: solve(i=1, target=1, current=[2,2,2])
│   │   │   │   │   │       ├── INCLUDE 3 → target=-2 → return
│   │   │   │   │   │       ├── BACKTRACK → current=[2,2,2]
│   │   │   │   │   │       └── EXCLUDE: solve(i=2, target=1) → (same as above, all fail)
│   │   │   │   ├── BACKTRACK → current=[2,2]
│   │   │   │   └── EXCLUDE: solve(i=1, target=3, current=[2,2])
│   │   │   │       └── (same subtree as SINGLE above — finds [2,2,3] again, already visited)
│   │   ├── BACKTRACK → current=[2]
│   │   └── EXCLUDE: solve(i=1, target=5, current=[2])
│   │       ├── INCLUDE 3 → current=[2,3]
│   │       │   ├── SINGLE: solve(i=2, target=2, current=[2,3]) → (all fail, same as above)
│   │       │   ├── MULTIPLE: solve(i=1, target=2, current=[2,3]) → (all fail)
│   │       │   ├── BACKTRACK → current=[2]
│   │       │   └── EXCLUDE: solve(i=2, target=5, current=[2]) → (all fail)
│   │       ...
│   │
├── BACKTRACK → current=[]
├── EXCLUDE: solve(i=1, target=7, current=[])
│   ├── INCLUDE 3 → current=[3]
│   │   ├── SINGLE: solve(i=2, target=4, current=[3])
│   │   │   ├── INCLUDE 6 → current=[3,6], target=-2 → return
│   │   │   ├── BACKTRACK → current=[3]
│   │   │   └── EXCLUDE: solve(i=3, target=4, current=[3])
│   │   │       ├── INCLUDE 7 → current=[3,7], target=-3 → return
│   │   │       ├── BACKTRACK → current=[3]
│   │   │       └── EXCLUDE: solve(i=4) → return (i==len)
│   │   ├── MULTIPLE: solve(i=1, target=4, current=[3])
│   │   │   ├── INCLUDE 3 → current=[3,3]
│   │   │   │   ├── SINGLE: solve(i=2, target=1, current=[3,3])
│   │   │   │   │   ├── INCLUDE 6 → target=-5 → return
│   │   │   │   │   ├── BACKTRACK → current=[3,3]
│   │   │   │   │   └── EXCLUDE: solve(i=3, target=1)
│   │   │   │   │       ├── INCLUDE 7 → target=-6 → return
│   │   │   │   │       ├── BACKTRACK → current=[3,3]
│   │   │   │   │       └── EXCLUDE: solve(i=4) → return (i==len)
│   │   │   │   ├── MULTIPLE: solve(i=1, target=1, current=[3,3])
│   │   │   │   │   ├── INCLUDE 3 → target=-2 → return
│   │   │   │   │   ├── BACKTRACK → current=[3,3]
│   │   │   │   │   └── EXCLUDE: solve(i=2, target=1) → (all fail)
│   │   │   │   ├── BACKTRACK → current=[3]
│   │   │   │   └── EXCLUDE: solve(i=2, target=4, current=[3])
│   │   │   │       └── (same as SINGLE above — all fail)
│   │   ├── BACKTRACK → current=[]
│   │   └── EXCLUDE: solve(i=2, target=7, current=[])
│   │       ├── INCLUDE 6 → current=[6]
│   │       │   ├── SINGLE: solve(i=3, target=1, current=[6])
│   │       │   │   ├── INCLUDE 7 → target=-6 → return
│   │       │   │   ├── BACKTRACK → current=[6]
│   │       │   │   └── EXCLUDE: solve(i=4) → return (i==len)
│   │       │   ├── MULTIPLE: solve(i=2, target=1, current=[6])
│   │       │   │   ├── INCLUDE 6 → target=-5 → return
│   │       │   │   ├── BACKTRACK → current=[6]
│   │       │   │   └── EXCLUDE: solve(i=3, target=1) → (same, all fail)
│   │       │   ├── BACKTRACK → current=[]
│   │       │   └── EXCLUDE: solve(i=3, target=7, current=[])
│   │       │       ├── INCLUDE 7 → current=[7]
│   │       │       │   ├── SINGLE: solve(i=4, target=0, current=[7])
│   │       │       │   │   └── i==len → return (note: target==0 check is BEFORE i==len check? No!)
│   │       │       │   │       Actually: i==4==len(arr) → return FIRST (base case order!)
│   │       │       │   ├── MULTIPLE: solve(i=3, target=0, current=[7])
│   │       │       │   │   └── ✅ target==0! → result.append([7])
│   │       │       │   ├── BACKTRACK → current=[]
│   │       │       │   └── EXCLUDE: solve(i=4, target=7) → return (i==len)
│   │       │       └── ... (no more elements)


'''
print("\n solution with two recursive call")

def solve(arr, i, target, current, result):

    # Base Case: Target achieved
    if target == 0:
        result.append(current[:])
        return

    # Base Case: Out of bounds
    if i == len(arr):
        return

    # Include (Take)
    if arr[i] <= target:
        current.append(arr[i])
        solve(arr, i, target - arr[i], current, result)
        current.pop()  # Backtrack

    # Exclude (Not Take)
    solve(arr, i + 1, target, current, result)


def combination_sum(arr, target):
    result = []
    current = []

    solve(arr, 0, target, current, result)

    return result


# Driver Code
arr = [2, 3, 6, 7]
target = 7

print(combination_sum(arr, target))
#-----------------------combination sum 2-----------------

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        result = []
        current = []

        self.solve(candidates, 0, target, current, result)

        return result

    def solve(self, arr, i, target, current, result):

        # Target achieved
        if target == 0:
            result.append(current[:])
            return

        # Out of bounds
        if i == len(arr):
            return

        # Take
        if arr[i] <= target:
            current.append(arr[i])
            self.solve(arr, i + 1, target - arr[i], current, result)
            current.pop()

        # Skip duplicate elements before "Not Take"
        while i + 1 < len(arr) and arr[i] == arr[i + 1]:
            i += 1

        # Not Take
        self.solve(arr, i + 1, target, current, result)


# Driver
sol = Solution()
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print("\n combination sum 2")
print(sol.combinationSum2(candidates, target))

'''
combinationSum2([10,1,2,7,6,1,5], target=8)
After sorting: arr = [1, 1, 2, 5, 6, 7, 10]

KEY LOGIC:
  - TAKE: use arr[i], move to i+1 (each element used at most once)
  - SKIP DUPLICATES: while arr[i] == arr[i+1], increment i
  - NOT TAKE: skip to i+1 (after duplicate skipping)

solve(arr=[1,1,2,5,6,7,10], i=0, target=8, current=[])
│
├── TAKE 1 → current=[1], solve(i=1, target=7, current=[1])
│   │
│   ├── TAKE 1 → current=[1,1], solve(i=2, target=6, current=[1,1])
│   │   │
│   │   ├── TAKE 2 → current=[1,1,2], solve(i=3, target=4, current=[1,1,2])
│   │   │   │
│   │   │   ├── TAKE 5 → current=[1,1,2,5], solve(i=4, target=-1)
│   │   │   │   └── arr[i]=5 > target=4? YES → skip TAKE
│   │   │   │       (actually 5 > 4, so TAKE is skipped)
│   │   │   │
│   │   │   ├── TAKE 5? → 5 > 4, skip TAKE
│   │   │   ├── NOT TAKE (no dups at i=3): solve(i=4, target=4, current=[1,1,2])
│   │   │   │   ├── TAKE 6? → 6 > 4, skip TAKE
│   │   │   │   ├── NOT TAKE: solve(i=5, target=4, current=[1,1,2])
│   │   │   │   │   ├── TAKE 7? → 7 > 4, skip TAKE
│   │   │   │   │   ├── NOT TAKE: solve(i=6, target=4, current=[1,1,2])
│   │   │   │   │   │   ├── TAKE 10? → 10 > 4, skip TAKE
│   │   │   │   │   │   └── NOT TAKE: solve(i=7) → return (i==len)
│   │   │   │   │   └── return
│   │   │   │   └── return
│   │   │   └── return
│   │   │
│   │   ├── TAKE 5 → current=[1,1,5], solve(i=4, target=1, current=[1,1,5])
│   │   │   │   (Wait, let me redo this more carefully)
│   │   │
│   │   │   Actually let me restart this subtree properly:
│   │   │
│   │   ├── TAKE 2 → current=[1,1,2], solve(i=3, target=4, current=[1,1,2])
│   │   │   ├── TAKE 5? → 5 > 4, SKIP TAKE
│   │   │   └── NOT TAKE: solve(i=4, target=4, current=[1,1,2])
│   │   │       ├── TAKE 6? → 6 > 4, SKIP TAKE
│   │   │       └── NOT TAKE: solve(i=5, target=4, current=[1,1,2])
│   │   │           ├── TAKE 7? → 7 > 4, SKIP TAKE
│   │   │           └── NOT TAKE: solve(i=6, target=4, current=[1,1,2])
│   │   │               ├── TAKE 10? → 10 > 4, SKIP TAKE
│   │   │               └── NOT TAKE: solve(i=7) → return (i==len)
│   │   │
│   │   ├── pop() → current=[1,1]
│   │   ├── NO DUPS at i=2 (arr[2]=2, arr[3]=5, different)
│   │   ├── NOT TAKE: solve(i=3, target=6, current=[1,1])
│   │   │   ├── TAKE 5 → current=[1,1,5], solve(i=4, target=1, current=[1,1,5])
│   │   │   │   ├── TAKE 6? → 6 > 1, SKIP TAKE
│   │   │   │   └── NOT TAKE: solve(i=5, target=1, current=[1,1,5])
│   │   │   │       ├── TAKE 7? → 7 > 1, SKIP TAKE
│   │   │   │       └── NOT TAKE: solve(i=6, target=1, current=[1,1,5])
│   │   │   │           ├── TAKE 10? → 10 > 1, SKIP TAKE
│   │   │   │           └── NOT TAKE: solve(i=7) → return (i==len)
│   │   │   ├── pop() → current=[1,1]
│   │   │   ├── NOT TAKE: solve(i=4, target=6, current=[1,1])
│   │   │   │   ├── TAKE 6 → current=[1,1,6], solve(i=5, target=0, current=[1,1,6])
│   │   │   │   │   └── ✅ target==0! result.append([1,1,6])
│   │   │   │   ├── pop() → current=[1,1]
│   │   │   │   ├── NOT TAKE: solve(i=5, target=6, current=[1,1])
│   │   │   │   │   ├── TAKE 7? → 7 > 6, SKIP TAKE
│   │   │   │   │   └── NOT TAKE: solve(i=6, target=6, current=[1,1])
│   │   │   │   │       ├── TAKE 10? → 10 > 6, SKIP TAKE
│   │   │   │   │       └── NOT TAKE: solve(i=7) → return (i==len)
│   │   │   │   └── return
│   │   │   └── return
│   │   └── return
│   │
│   ├── pop() → current=[1]
│   ├── SKIP DUPS: arr[1]=1 == arr[2]? NO (arr[2]=2), no skip
│   │   (Wait: we're at i=1 after TAKE. For NOT TAKE, check dups at i=1)
│   │   arr[1]=1, arr[2]=2 → different, no skip
│   ├── NOT TAKE: solve(i=2, target=7, current=[1])
│   │   │
│   │   ├── TAKE 2 → current=[1,2], solve(i=3, target=5, current=[1,2])
│   │   │   ├── TAKE 5 → current=[1,2,5], solve(i=4, target=0, current=[1,2,5])
│   │   │   │   └── ✅ target==0! result.append([1,2,5])
│   │   │   ├── pop() → current=[1,2]
│   │   │   ├── NOT TAKE: solve(i=4, target=5, current=[1,2])
│   │   │   │   ├── TAKE 6? → 6 > 5, SKIP TAKE
│   │   │   │   └── NOT TAKE: solve(i=5, target=5, current=[1,2])
│   │   │   │       ├── TAKE 7? → 7 > 5, SKIP TAKE
│   │   │   │       └── NOT TAKE: solve(i=6, target=5, current=[1,2])
│   │   │   │           ├── TAKE 10? → 10 > 5, SKIP TAKE
│   │   │   │           └── NOT TAKE: solve(i=7) → return (i==len)
│   │   │   └── return
│   │   │
│   │   ├── pop() → current=[1]
│   │   ├── NOT TAKE: solve(i=3, target=7, current=[1])
│   │   │   ├── TAKE 5 → current=[1,5], solve(i=4, target=2, current=[1,5])
│   │   │   │   ├── TAKE 6? → 6 > 2, SKIP TAKE
│   │   │   │   └── NOT TAKE: solve(i=5, target=2, current=[1,5])
│   │   │   │       ├── TAKE 7? → 7 > 2, SKIP TAKE
│   │   │   │       └── NOT TAKE: solve(i=6) → TAKE 10? 10>2 → solve(i=7) → return
│   │   │   ├── pop() → current=[1]
│   │   │   ├── NOT TAKE: solve(i=4, target=7, current=[1])
│   │   │   │   ├── TAKE 6 → current=[1,6], solve(i=5, target=1, current=[1,6])
│   │   │   │   │   ├── TAKE 7? → 7 > 1, SKIP TAKE
│   │   │   │   │   └── NOT TAKE: solve(i=6) → 10>1 → solve(i=7) → return
│   │   │   │   ├── pop() → current=[1]
│   │   │   │   ├── NOT TAKE: solve(i=5, target=7, current=[1])
│   │   │   │   │   ├── TAKE 7 → current=[1,7], solve(i=6, target=0, current=[1,7])
│   │   │   │   │   │   └── ✅ target==0! result.append([1,7])
│   │   │   │   │   ├── pop() → current=[1]
│   │   │   │   │   ├── NOT TAKE: solve(i=6, target=7, current=[1])
│   │   │   │   │   │   ├── TAKE 10? → 10 > 7, SKIP TAKE
│   │   │   │   │   │   └── NOT TAKE: solve(i=7) → return (i==len)
│   │   │   │   │   └── return
│   │   │   │   └── return
│   │   │   └── return
│   │   └── return
│   └── return
│
├── pop() → current=[]
├── SKIP DUPS: arr[0]=1 == arr[1]=1? YES → i becomes 1
│   (now i=1, no more dups: arr[1]=1, arr[2]=2, stop)
├── NOT TAKE: solve(i=2, target=8, current=[])
│   │
│   ├── TAKE 2 → current=[2], solve(i=3, target=6, current=[2])
│   │   ├── TAKE 5 → current=[2,5], solve(i=4, target=1, current=[2,5])
│   │   │   ├── TAKE 6? → 6 > 1, SKIP TAKE
│   │   │   └── NOT TAKE: solve(i=5) → 7>1 → solve(i=6) → 10>1 → solve(i=7) → return
│   │   ├── pop() → current=[2]
│   │   ├── NOT TAKE: solve(i=4, target=6, current=[2])
│   │   │   ├── TAKE 6 → current=[2,6], solve(i=5, target=0, current=[2,6])
│   │   │   │   └── ✅ target==0! result.append([2,6])
│   │   │   ├── pop() → current=[2]
│   │   │   ├── NOT TAKE: solve(i=5, target=6, current=[2])
│   │   │   │   ├── TAKE 7? → 7 > 6, SKIP TAKE
│   │   │   │   └── NOT TAKE: solve(i=6, target=6, current=[2])
│   │   │   │       ├── TAKE 10? → 10 > 6, SKIP TAKE
│   │   │   │       └── NOT TAKE: solve(i=7) → return (i==len)
│   │   │   └── return
│   │   └── return
│   │
│   ├── pop() → current=[]
│   ├── NOT TAKE: solve(i=3, target=8, current=[])
│   │   ├── TAKE 5 → current=[5], solve(i=4, target=3, current=[5])
│   │   │   ├── TAKE 6? → 6 > 3, SKIP TAKE
│   │   │   └── NOT TAKE: solve(i=5, target=3, current=[5])
│   │   │       ├── TAKE 7? → 7 > 3, SKIP TAKE
│   │   │       └── NOT TAKE: solve(i=6) → 10>3 → solve(i=7) → return
│   │   ├── pop() → current=[]
│   │   ├── NOT TAKE: solve(i=4, target=8, current=[])
│   │   │   ├── TAKE 6 → current=[6], solve(i=5, target=2, current=[6])
│   │   │   │   ├── TAKE 7? → 7 > 2, SKIP TAKE
│   │   │   │   └── NOT TAKE: solve(i=6) → 10>2 → solve(i=7) → return
│   │   │   ├── pop() → current=[]
│   │   │   ├── NOT TAKE: solve(i=5, target=8, current=[])
│   │   │   │   ├── TAKE 7 → current=[7], solve(i=6, target=1, current=[7])
│   │   │   │   │   ├── TAKE 10? → 10 > 1, SKIP TAKE
│   │   │   │   │   └── NOT TAKE: solve(i=7) → return (i==len)
│   │   │   │   ├── pop() → current=[]
│   │   │   │   ├── NOT TAKE: solve(i=6, target=8, current=[])
│   │   │   │   │   ├── TAKE 10? → 10 > 8, SKIP TAKE
│   │   │   │   │   └── NOT TAKE: solve(i=7) → return (i==len)
│   │   │   │   └── return
│   │   │   └── return
│   │   └── return
│   └── return
└── return

═══════════════════════════════════════════════════════════
SOLUTIONS FOUND (in order):
═══════════════════════════════════════════════════════════

✅ [1, 1, 6]    ← Path: TAKE 1 → TAKE 1 → NOT TAKE 2 → NOT TAKE 5 → TAKE 6
✅ [1, 2, 5]    ← Path: TAKE 1 → NOT TAKE 1 → TAKE 2 → TAKE 5
✅ [1, 7]       ← Path: TAKE 1 → NOT TAKE 1 → NOT TAKE 2 → NOT TAKE 5 → NOT TAKE 6 → TAKE 7
✅ [2, 6]       ← Path: NOT TAKE 1(skip dup) → TAKE 2 → NOT TAKE 5 → TAKE 6

Final Output: [[1,1,6], [1,2,5], [1,7], [2,6]]

═══════════════════════════════════════════════════════════
HOW DUPLICATE SKIPPING WORKS:
═══════════════════════════════════════════════════════════

arr = [1, 1, 2, 5, 6, 7, 10]  (sorted)
       ^  ^
       duplicates

At i=0: After TAKE arr[0]=1 and backtrack:
  - Check: arr[0]==arr[1]? (1==1) YES → i becomes 1
  - Check: arr[1]==arr[2]? (1==2) NO → stop
  - NOT TAKE jumps to i=2 (skipping the second 1)

WHY? If we already explored "TAKE first 1", then "NOT TAKE first 1, TAKE second 1"
would produce the same subsets. The skip prevents this duplication.

Example without skip: [1,_,2,5,...] and [_,1,2,5,...] both give [1,2,5]
With skip: only the TAKE path uses 1, NOT TAKE skips ALL 1s → no duplicates!
'''


##Generate Parathesis

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack=[]
        res=[]

        def backtrack(openN,closeN):

            if openN==closeN==n:
                res.append("".join(stack))

            if openN<n:
                stack.append("(")
                backtrack(openN+1,closeN)
                stack.pop()
            if closeN<openN:
                stack.append(")")
                backtrack(openN,closeN+1)
                stack.pop()

        backtrack(0,0)
        
###phone letter generation code ############

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]

        digitTochar={

            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }


        def backtrack(i,currstr):

            if len(currstr) == len(digits):
                res.append(currstr)
                return

            for c in digitTochar[digits[i]]:
                backtrack(i+1,currstr+c)

        if digits:
            backtrack(0,"")
        return res
        
#permutation

'''
Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
'''

print('\n permutation')
def permutation(nums):
    
    result=[]
    
    visited =set()
    
    if (len(nums)==1):
        return[nums[:]]
    
    for i in range(len(nums)):
        n=nums.pop(0)
        
        perms=permutation(nums)
        
        for per in perms:
            per.append(n)

            t = tuple(per)      # Convert list -> tuple

            if t not in visited:
                visited.add(t)
                result.append(per)
        nums.append(n)
    return result

nums=[1,1,2]

print(permutation(nums))
