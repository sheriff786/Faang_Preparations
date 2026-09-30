'''
Problem
  
Kth Largest In A Stream
Given an initial list along with another list of numbers to be appended with the initial list and an integer k, return an array consisting of the k-th largest element after adding each element from the first list to the second list.

Example
{
"k": 2,
"initial_stream": [4, 6],
"append_stream": [5, 2, 20]
}
Output:

[5, 5, 6]
Append	Stream	Sorted Stream	2nd largest
5	[4, 6, 5]	[4, 5, 6]	5
2	[4, 6, 5, 2]	[2, 4, 5, 6]	5
20	[4, 6, 5, 2, 20]	[2, 4, 5, 6, 20]	6
Notes
The stream can contain duplicates.
Constraints:

1 <= length of both lists <= 105
1 <= k <= length of initial list + 1
0 <= any value in the list <= 109
.
.
.
.
.

Autocomplete

I/O
    #brute force approach


 
00:02:22
Sa
'''


def kth_largest(k, initial_stream, append_stream):
    """
    Args:
     k(int32)
     initial_stream(list_int32)
     append_stream(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    #brute force approach
    # arr=[]
    # for i in range(len(append_stream)):
        
    #     initial_stream.append(append_stream[i])
    #     initial_stream.sort()
    #     arr.append(initial_stream[-k])
        
    # return arr
    
    #optimize solution to use heap
    
    import heapq

# def kth_largest(k, initial_stream, append_stream):
    heap = []

    for num in initial_stream:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    result = []

    for num in append_stream:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

        result.append(heap[0])

    return result


'''
Kth Largest In An Array
Given an array of integers, find the k-th largest number in it.

Example One
{
"numbers": [5, 1, 10, 3, 2],
"k": 2
}
Output:

5
Example Two
{
"numbers": [4, 1, 2, 2, 3],
"k": 4
}
Output:

2
Notes
Constraints:

1 <= array size <= 3 * 105
-109 <= array elements <= 109
1 <= k <= array size


'''

def kth_largest_in_an_array(numbers, k):
    """
    Args:
     numbers(list_int32)
     k(int32)
    Returns:
     int32
    """
    # Write your code here.
    import heapq
    heap=[]
     
    for x in numbers:
        heapq.heappush(heap, x)
    
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]  
    
    #optimize solution of complexity O(n)
    
    # def kth_largest_in_an_array(numbers, k):
    # target = len(numbers) - k

    # left = 0
    # right = len(numbers) - 1

    # while left <= right:
    #     pivot = numbers[right]

    #     p = left

    #     for i in range(left, right):
    #         if numbers[i] <= pivot:
    #             numbers[p], numbers[i] = numbers[i], numbers[p]
    #             p += 1

    #     numbers[p], numbers[right] = numbers[right], numbers[p]

    #     if p == target:
    #         return numbers[p]

    #     elif p < target:
    #         left = p + 1

    #     else:
    #         right = p - 1
            
        
'''

Yes. The easiest way to remember Quickselect is to connect it to QuickSort, but remember one crucial difference.

1. The core trick 🧠

Think:

QuickSort → partition BOTH sides
Quickselect → partition ONLY the side containing my answer

That's the entire idea.

Example:

[5, 1, 10, 3, 2]

              pivot
                ↓
[1, 2 | 10, 3, 5]

Once pivot 2 is at index 1, you know:

left side  → smaller/equal
right side → larger

If your target is on the right, forget the left side.

2. The magic formula for Kth Largest

This is worth memorizing:

kth largest → index = n - k

Example:

n = 5
k = 2

target = 5 - 2 = 3

Sorted:

[1, 2, 3, 5, 10]
          ↑
        index 3

For kth smallest:

target = k - 1

So:

Kth Smallest → k - 1
Kth Largest  → n - k
3. The three cases — easiest trick

After partitioning, you get:

p = pivot's final index
target = where your answer should be

Just compare:

       p ? target
Case 1: p == target

🎯 Found it

if p == target:
    return numbers[p]
Case 2: p < target

Your answer is RIGHT.

elif p < target:
    left = p + 1

Memory trick:

Pivot is too LEFT → go RIGHT

        p          target
        ↓             ↓
[-------P-------------X---->]
                GO RIGHT →
Case 3: p > target

Your answer is LEFT.

else:
    right = p - 1

Memory trick:

Pivot is too RIGHT → go LEFT

target       p
  ↓          ↓
[-----X------P-------]
      ← GO LEFT
One-line memory trick

Compare p with target: equal = answer, smaller = right, bigger = left.

p == target → FOUND
p < target  → RIGHT
p > target  → LEFT
4. When should you think about Quickselect?

Whenever the question sounds like:

"I need the Kth..."

Examples:

Kth largest element
Kth smallest element
Kth highest salary
Kth lowest price
Kth closest point
Kth largest number
Median
Top K elements

But there is an important distinction.

If they need ONLY one element

Think:

Kth smallest → Quickselect
Kth largest  → Quickselect
Median        → Quickselect

Because you don't need the entire array sorted.

5. Quickselect vs Heap

This is particularly important for interviews.

Suppose:

n = 1,000,000
k = 5

You want the 5th largest.

Heap

Maintain only 5 elements:

O(n log k)

Since k = 5, this is approximately:

O(n)

Very good.

Quickselect

Average:

O(n)

Also very good.

So how do you decide?

Rule of thumb
Need kth element?
        ↓
   Quickselect
Need streaming data?
        ↓
      Heap
Need top K elements?
        ↓
      Heap
Need sorted entire array?
        ↓
      Sorting
6. The BIG clue: "Don't sort the whole array"

If interviewer says:

Find kth largest without sorting.

Immediately think:

Quickselect

Because sorting gives:

O(n log n)

Quickselect gives:

O(n) average
7. Problems where Quickselect can appear
Direct
Find kth largest element
Find kth smallest element
Find median
Find percentile
Related
Find kth closest point to origin
Find kth largest distance
Find kth smallest value
Find element with rank k

The common pattern is:

I need an element at a particular rank, not the whole sorted collection.

That's the strongest signal for Quickselect.

8. Quickselect mental template

When you see a problem, run this checklist:

1. Do I need an element with a specific rank?
             ↓
            YES
             ↓
2. Do I need the whole array sorted?
             ↓
            NO
             ↓
3. Can I partition around a pivot?
             ↓
            YES
             ↓
        QUICKSELECT

Then remember:

Kth smallest → target = k - 1
Kth largest  → target = n - k

Then:

partition
   ↓
p == target → answer
p < target  → right
p > target  → left
🔥 Interview cheat sheet
                    RANK PROBLEM
                         │
             ┌───────────┴───────────┐
             │                       │
       One kth element           Top K elements
             │                       │
        Quickselect                 Heap
             │
       target = index
             │
    ┌────────┼────────┐
    ↓        ↓        ↓
 p == t    p < t    p > t
  FOUND     RIGHT     LEFT

If you remember just p vs target, you can reconstruct almost the entire Quickselect algorithm during an interview.

'''

         
'''
Online median problem
'''
    
    
'''
intersecton of array
Problem
  
Intersection Of Three Sorted Arrays
Given three arrays sorted in the ascending order, return their intersection sorted array in the ascending order.

Example One
{
"arr1": [2, 5, 10],
"arr2": [2, 3, 4, 10],
"arr3": [2, 4, 10]
}
Output:

[2, 10]
Example Two
{
"arr1": [1, 2, 3],
"arr2": [],
"arr3": [2, 2]
}
Output:

[-1]
Example Three
{
"arr1": [1, 2, 2, 2, 9],
"arr2": [1, 1, 2, 2],
"arr3": [1, 1, 1, 2, 2, 2]
}
Output:

[1, 2, 2]
Notes
If the intersection is empty, return an array with one element -1.
Constraints:

0 <= length of each given array <= 105
0 <= any value in a given array <= 2 * 106

'''

def find_intersection(arr1, arr2, arr3):
    """
    Args:
     arr1(list_int32)
     arr2(list_int32)
     arr3(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    #Brute force solution
    
    # result = []

    # for x in arr1:
    #     if x in arr2 and x in arr3:
    #         result.append(x)

    # return result if result else [-1]
    # #time complexity O(N²)
    # # def intersection_of_three(arr1, arr2, arr3):
    # from collections import Counter

    # c1 = Counter(arr1)
    # c2 = Counter(arr2)
    # c3 = Counter(arr3)

    # result = []

    # for x in c1:
    #     if x in c2 and x in c3:
    #         count = min(c1[x], c2[x], c3[x])

    #         result.extend([x] * count)

    # return result if result else [-1]
    '''
    Time:  O(n + m + p)
    Space: O(n + m + p)
    
    '''
    # def intersection_of_three(arr1, arr2, arr3):
    i = j = k = 0
    result = []

    while i < len(arr1) and j < len(arr2) and k < len(arr3):

        if arr1[i] == arr2[j] == arr3[k]:
            result.append(arr1[i])

            i += 1
            j += 1
            k += 1

        elif arr1[i] < arr2[j]:
            i += 1

        elif arr2[j] < arr3[k]:
            j += 1

        else:
            k += 1

    return result if result else [-1]


