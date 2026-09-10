#Segregate Even And Odd Numbers

# Given an array of numbers, rearrange them in-place so that even numbers appear before odd ones.

# Example
# {
# "numbers": [1, 2, 3, 4]
# }
# Output:

# [4, 2, 3, 1]
# The order within the group of even numbers does not matter; same with odd numbers. So the following are also correct outputs: [4, 2, 1, 3], [2, 4, 1, 3], [2, 4, 3, 1]. 

#i got two approaches
# brute force
#     use %2 to check division whether is even or odd
#     and get three array even array and odd aray and merge array
#     once you check append it as per respective places and then merge it + operator

#2# optimize approach two pointer
def segregate_evens_and_odds(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    left=0
    right = len(numbers)-1
    
    while(left<right):
        
        if numbers[left]%2==0:
            left+=1
        elif numbers[right]%2!=0:
            right-=1
        else:
            numbers[left],numbers[right]=numbers[right],numbers[left]
            left+=1
            right-=1
        
    
    return numbers

#question 2
#merge two elements

def merge_one_into_another(first, second):
    # n = len(first)

    # i = n - 1          # last element of first
    # j = n - 1          # last non-zero element in second
    # k = 2 * n - 1      # last position in second

    # # Merge from back
    # while i >= 0 and j >= 0:
    #     if first[i] > second[j]:
    #         second[k] = first[i]
    #         i -= 1
    #     else:
    #         second[k] = second[j]
    #         j -= 1
    #     k -= 1

    # # Remaining elements from first
    # while i >= 0:
    #     second[k] = first[i]
    #     i -= 1
    #     k -= 1

    # return second
    arr = []
    
    l = 0
    r = 0
    
    n = len(first)
    m = len(second) - len(first)   # actual elements in second

    while l < n and r < m:
        if first[l] < second[r]:
            arr.append(first[l])
            l += 1
        else:
            arr.append(second[r])
            r += 1

    while l < n:
        arr.append(first[l])
        l += 1

    while r < m:
        arr.append(second[r])
        r += 1
        
#3 question on dutch flag
'''
Dutch National Flag
Given some balls of three colors arranged in a line, rearrange them such that all the red balls go first, then green and then blue ones.

Do rearrange the balls in place. A solution that simply counts colors and overwrites the array is not the one we are looking for.

This is an important problem in search algorithms theory proposed by Dutch computer scientist Edsger Dijkstra. Dutch national flag has three colors (albeit different from ones used in this problem).

Example
{
"balls": ["G", "B", "G", "G", "R", "B", "R", "G"]
}
Output:

["R", "R", "G", "G", "G", "G", "B", "B"]
There are a total of 2 red, 4 green and 2 blue balls. In this order they appear in the correct output.


'''

'''
Approaches i got
first at linear search i will create three dictionary and add those balss respected to it and at the end merge it like array_red+array_green+array_blue 

second approach apply merge sort to have the swapping condition on r,g,b

third approach have three pointer --> low,high,mid

'''

def dutch_flag_sort(balls):
    low = 0
    mid = 0
    high = len(balls) - 1

    while mid <= high:
        if balls[mid] == "R":
            balls[low], balls[mid] = balls[mid], balls[low]
            low += 1
            mid += 1

        elif balls[mid] == "G":
            mid += 1

        else:  # "B"
            balls[mid], balls[high] = balls[high], balls[mid]
            high -= 1

    return balls
# #question 3 two sum in sorted array 
# have three approcach
# 1.brute force run the loops
# 2.two pointer
# 3.binary search
# 4.hasmap

# #now if two sum array is not sorted then 
# 1.brute force
# 2.hashmap
# 3.sort the array then appy two pointer

def pair_sum_sorted_array(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    seen = {}
    
    for i in range(0,len(numbers)):
        diff=target-numbers[i]
        
        if diff in seen:
            return[seen[diff],i]
        seen[numbers[i]]=i
            
    return [-1,-1]

# Question attend meeting
# Attend Meetings
# Given a list of meeting intervals where each interval consists of a start and an end time, check if a person can attend all the given meetings such that only one meeting can be attended at a time.

# Example One
# {
# "intervals": [
# [1, 5],
# [5, 8],
# [10, 15]
# ]
# }
# Output:

# 1
# As the above intervals are non-overlapping intervals, it means a person can attend all these meetings.

# Example Two
# {
# "intervals": [
# [1, 5],
# [4, 8]
# ]
# }
# Output:

# 0
# Time 4 - 5 is overlapping in the first and second intervals.

# Notes
# A new meeting can start at the same time the previous one ended.
# Constraints:

# 1 <= number of intervals <= 105
# 0 <= start time < end time <= 109
'''

approach i got is brute force where we will try to conver inputes from list inside list to list only like this

[1,5,5,8,10,15] and if all elements are sorted then return 1 if not then return 0

2nd approach 

use two pointer like

prev as [0][1]
current as [1][0] and compare current < prev is return 0 in whole for loop if not outside return 1

'''
def can_attend_all_meetings(intervals):
    """
    Args:
     intervals(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    # Step 2: check overlap
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        prev_end = intervals[i-1][1]
        curr_start = intervals[i][0]
        
        if curr_start < prev_end:
            return 0  # overlap
    
    return 1  # no overlap

#questions Sort All Characters
# Given a list of characters, sort it in the non-decreasing order based on ASCII values of characters.

# Example
# {
# "arr": ["a", "s", "d", "f", "g", "*", "&", "!", "z", "y"]
# }
# Output:

# ["!", "&", "*", "a", "d", "f", "g", "s", "y", "z"]
# Notes
# Constraints:

# 1 <= length of the list <= 100000
# Input list consists of alphanumeric characters and these ones: !, @, #, $, %, ^, &, *, (, ).

def sort_array(arr):
    """
    Args:
     arr(list_char)
    Returns:
     list_char
    """
    # Write your code here.
    count = [0] * 128

    # Count frequency
    for ch in arr:
        count[ord(ch)] += 1

    result = []

    # Traverse ASCII order
    for i in range(128):
        while count[i] > 0:
            result.append(chr(i))
            count[i] -= 1

    return result
#Question four billon
'''
Four Billion
Given four billion of 32-bit integers, return any one that’s not among them. Assume you have 1 GiB (10243 bytes) of memory.

Follow up: what if you only have 10 MiB of memory?

Example One
{
"arr": [0, 1, 2, 3]
}
Output:

4
Any number in the [4 .. 232) range is a correct answer.

Example Two
{
"arr": [4294967295, 399999999, 0]
}
Output:

1
Here again 1 is just one of many correct answers.

Notes
Even though there won’t actually be a test with four billion numbers, do design and write a solution for four billion.
Constraints:

1 <= length of input array <= 200000
0 <= element of input array < 232
'''


def find_integer(arr):
    """
    Args:
     arr(list_int64)
    Returns:
     int64
    """
    # Write your code here.
    # def find_missing(arr):
    BUCKET_SIZE = 2**16       # 65,536 numbers per bucket
    NUM_BUCKETS = 2**16       # 65,536 buckets

    count = [0] * NUM_BUCKETS

    # Count numbers in each bucket
    for num in arr:
        bucket = num // BUCKET_SIZE
        count[bucket] += 1

    # Find a bucket that is not completely occupied
    for bucket in range(NUM_BUCKETS):

        start = bucket * BUCKET_SIZE
        end = start + BUCKET_SIZE

        if count[bucket] < BUCKET_SIZE:
            break

    # Now search only inside this bucket
    seen = set()

    for num in arr:
        if start <= num < end:
            seen.add(num)

    # Find missing number in this bucket
    for num in range(start, end):
        if num not in seen:
            return num

# Nearest neighbour

'''
Nearest Neighbors
Given coordinates of a point p and n other points on a two-dimensional surface, find k points out of n which are the nearest to point p.

Distance is measured by the standard Euclidean method.

Example One
{
"p_x": 1,
"p_y": 1,
"k": 1,
"n_points": [
[0, 0],
[1, 0]
]
}
Output:

[
[1, 0]
]
The distance of point {0, 0} from point p{1, 1} is sqrt(2) and that of point {1, 0} is 1. We need to choose 1(k) point having the minimum distance from point p. So it is {1, 0}.

Example Two
{
"p_x": 1,
"p_y": 1,
"k": 2,
"n_points": [
[1, 0],
[2, 1],
[0, 1]
]
}
Output:

[
[1, 0],
[2, 1]
]
We can see that there are all the points are at the same distance from point p. So the answer can be any 2 points. Here {{1, 0}, {0, 1}} and {{2, 1}, {0, 1}} are all equally acceptable answers.

Notes
Constraints:

1 <= n <= 100000
k <= n
-1000000000 <= coordinates of points <=1000000000

'''
def nearest_neighbors(p_x, p_y, k, n_points):
    distances = []

    # Calculate squared distance for every point
    for point in n_points:
        x, y = point

        distance = (x - p_x) ** 2 + (y - p_y) ** 2

        distances.append((distance, point))

    # Sort based on distance
    distances.sort(key=lambda x: x[0])

    # Take first k points
    result = []

    for i in range(k):
        result.append(distances[i][1])

    return result

import heapq

def nearest_neighbors(p_x, p_y, k, n_points):
    heap = []

    for point in n_points:
        x, y = point

        distance = (x - p_x) ** 2 + (y - p_y) ** 2

        # Negative distance → simulate max heap
        heapq.heappush(heap, (-distance, x, y))

        # Keep only k points
        if len(heap) > k:
            heapq.heappop(heap)

    return [[x, y] for _, x, y in heap]

#question top k-frequent elements
'''
Top K Frequent Elements
Given an integer array and a number k, find the k most frequent elements in the array.

Example One
{
"arr": [1, 2, 3, 2, 4, 3, 1],
"k": 2
}
Output:

[3, 1]
Example Two
{
"arr": [1, 2, 1, 2, 3, 1],
"k": 1
}
Output:

[1]
Notes
If multiple answers exist, return any.
The order of numbers in the output array does not matter.
Constraints:

1 <= length of the given array <= 3 * 105
0 <= array element <= 3 * 105
1 <= k <= number of unique elements in the array

'''
def top_k_frequent(arr, k):
    freq = {}

    # Count frequency
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Sort by frequency
    sorted_freq = sorted(
        freq.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # Get top k
    result = []

    for i in range(k):
        result.append(sorted_freq[i][0])

    return result

import heapq

def top_k_frequent(arr, k):
    # Step 1: Count frequency
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Step 2: Min heap of size k
    heap = []

    for num, count in freq.items():
        heapq.heappush(heap, (count, num))

        # Keep only k elements
        if len(heap) > k:
            heapq.heappop(heap)

    # Step 3: Extract elements
    result = []

    while heap:
        count, num = heapq.heappop(heap)
        result.append(num)

    return result

#using bucket sort
def top_k_frequent(arr, k):
    # 1. Count frequency
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # 2. Create buckets
    buckets = [[] for _ in range(len(arr) + 1)]

    # 3. Put numbers into frequency bucket
    for num, count in freq.items():
        buckets[count].append(num)

    # 4. Traverse from highest frequency
    result = []

    for count in range(len(arr), 0, -1):
        for num in buckets[count]:
            result.append(num)

            if len(result) == k:
                return result

    return result


