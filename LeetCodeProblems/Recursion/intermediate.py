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