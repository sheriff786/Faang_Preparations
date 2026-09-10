"""
==========================================================================================
                          SORTING ALGORITHMS - THE COMPLETE GUIDE
==========================================================================================

WHAT IS SORTING?
    Rearranging elements of a list into a defined order (ascending / descending).

WHY LEARN ALL OF THEM?
    - FAANG interviews test WHY you pick one over another (stability, memory, data size).
    - Understanding trade-offs (time vs space vs stability) is the real skill.

------------------------------------------------------------------------------------------
                              QUICK CHEAT-SHEET TABLE
------------------------------------------------------------------------------------------
Algorithm       | Best        | Average     | Worst       | Space   | Stable | In-Place
----------------|-------------|-------------|-------------|---------|--------|---------
Bubble Sort     | O(n)        | O(n^2)      | O(n^2)      | O(1)    | Yes    | Yes
Selection Sort  | O(n^2)      | O(n^2)      | O(n^2)      | O(1)    | No     | Yes
Insertion Sort  | O(n)        | O(n^2)      | O(n^2)      | O(1)    | Yes    | Yes
Merge Sort      | O(n log n)  | O(n log n)  | O(n log n)  | O(n)    | Yes    | No
Quick Sort      | O(n log n)  | O(n log n)  | O(n^2)      | O(log n)| No     | Yes
Heap Sort       | O(n log n)  | O(n log n)  | O(n log n)  | O(1)    | No     | Yes
Counting Sort   | O(n + k)    | O(n + k)    | O(n + k)    | O(k)    | Yes    | No
Radix Sort      | O(d*(n+k))  | O(d*(n+k))  | O(d*(n+k))  | O(n+k)  | Yes    | No
Bucket Sort     | O(n + k)    | O(n + k)    | O(n^2)      | O(n)    | Yes    | No

    n = number of elements, k = range of values, d = number of digits

------------------------------------------------------------------------------------------
                          TRICKS TO REMEMBER (MEMORY HOOKS)
------------------------------------------------------------------------------------------
1. "BSI are the O(n^2) squad"  -> Bubble, Selection, Insertion are the simple O(n^2) ones.
2. "MQH are the O(n log n) squad" -> Merge, Quick, Heap are the fast comparison sorts.
3. "CRB break the n log n barrier" -> Counting, Radix, Bucket are non-comparison (linear-ish).
4. STABLE sorts spell "BIM-CRB": Bubble, Insertion, Merge, Counting, Radix, Bucket.
   (NOT stable: Selection, Quick, Heap  -> remember "SQH swap far apart = unstable".)
5. IN-PLACE (O(1) extra): Bubble, Selection, Insertion, Heap, Quick(log n stack).
   NOT in-place: Merge, Counting, Radix, Bucket (need extra arrays).
6. Lower bound of ANY comparison sort = O(n log n). To beat it you must NOT compare
   (that is exactly what Counting/Radix/Bucket do).
7. Quick Sort = fast in practice (cache friendly) but O(n^2) worst case (already sorted
   with bad pivot). Merge Sort = guaranteed O(n log n) but needs O(n) space.
8. Python's built-in sorted() / list.sort() uses TIMSORT (Merge + Insertion hybrid),
   stable, O(n log n).
==========================================================================================
"""


# ==========================================================================================
# 1. BUBBLE SORT
# ==========================================================================================
# IDEA: Repeatedly swap adjacent elements if they are in the wrong order. The largest
#       element "bubbles up" to the end each pass.
#
# TIME : Best O(n) [already sorted, with early-exit flag], Avg/Worst O(n^2)
# SPACE: O(1)  | STABLE: Yes | IN-PLACE: Yes
#
# TRICK: "Bubble = neighbours fight, big one floats to the top."
#
# DRY RUN on [5, 1, 4, 2]:
#   Pass 1: (5,1)->swap [1,5,4,2] | (5,4)->swap [1,4,5,2] | (5,2)->swap [1,4,2,5]
#   Pass 2: (1,4)->ok   | (4,2)->swap [1,2,4,5] | (4,5)->ok
#   Pass 3: no swaps -> array sorted -> early exit
#   RESULT: [1, 2, 4, 5]
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        # after each pass, last i elements are already in place
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # already sorted -> stop early
            break
    return arr


# ==========================================================================================
# 2. SELECTION SORT
# ==========================================================================================
# IDEA: Find the minimum from the unsorted part and place it at the front. Repeat.
#
# TIME : Best/Avg/Worst all O(n^2) (always scans the rest)
# SPACE: O(1)  | STABLE: No | IN-PLACE: Yes
#
# TRICK: "Select the smallest, swap it to the front." Fewest swaps (at most n-1).
#
# DRY RUN on [5, 1, 4, 2]:
#   i=0: min in [5,1,4,2] is 1 -> swap -> [1,5,4,2]
#   i=1: min in [5,4,2]   is 2 -> swap -> [1,2,4,5]
#   i=2: min in [4,5]     is 4 -> no swap -> [1,2,4,5]
#   RESULT: [1, 2, 4, 5]
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# ==========================================================================================
# 3. INSERTION SORT
# ==========================================================================================
# IDEA: Build the sorted part one element at a time by inserting each new element into its
#       correct position among the already-sorted elements (like sorting playing cards).
#
# TIME : Best O(n) [already sorted], Avg/Worst O(n^2)
# SPACE: O(1)  | STABLE: Yes | IN-PLACE: Yes
#
# TRICK: "Insertion = sorting cards in your hand." Great for small or nearly-sorted arrays.
#
# DRY RUN on [5, 1, 4, 2]:
#   key=1: shift 5 -> [5,5,4,2] insert -> [1,5,4,2]
#   key=4: shift 5 -> [1,5,5,2] insert -> [1,4,5,2]
#   key=2: shift 5 -> shift 4 -> [1,4,4,5] insert -> [1,2,4,5]
#   RESULT: [1, 2, 4, 5]
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # shift elements greater than key one position to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# ==========================================================================================
# 4. MERGE SORT  (Divide & Conquer)
# ==========================================================================================
# IDEA: Split array in half, recursively sort each half, then MERGE the two sorted halves.
#
# TIME : Best/Avg/Worst all O(n log n)  (log n levels, O(n) merge per level)
# SPACE: O(n)  | STABLE: Yes | IN-PLACE: No
#
# TRICK: "Divide till single, then merge like a zipper." Guaranteed n log n, best for
#        linked lists and external sorting (huge files that don't fit in memory).
#
# DRY RUN on [5, 1, 4, 2]:
#   split -> [5,1] and [4,2]
#   [5,1] -> [5],[1] -> merge -> [1,5]
#   [4,2] -> [4],[2] -> merge -> [2,4]
#   merge [1,5] & [2,4] -> compare 1<2 ->1 | 5>2 ->2 | 5>4 ->4 | 5 -> [1,2,4,5]
#   RESULT: [1, 2, 4, 5]
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        # "<=" keeps it STABLE (equal elements keep original order)
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ==========================================================================================
# 5. QUICK SORT  (Divide & Conquer)
# ==========================================================================================
# IDEA: Pick a PIVOT, partition array so smaller elements go left and larger go right,
#       then recursively sort both sides. Pivot lands in its final position each partition.
#
# TIME : Best/Avg O(n log n), Worst O(n^2) [bad pivot on sorted data]
# SPACE: O(log n) recursion stack | STABLE: No | IN-PLACE: Yes
#
# TRICK: "Pick pivot, partition, party on both sides." Fastest in practice (cache friendly).
#        Avoid worst case with random / median-of-three pivot.
#
# DRY RUN on [5, 1, 4, 2] (pivot = last element):
#   pivot=2 -> partition: 1<2 left, 5>2, 4>2 -> [1] 2 [5,4]
#   left [1] sorted. right [5,4] pivot=4 -> [ ] 4 [5] -> [4,5]
#   RESULT: [1, 2, 4, 5]
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_idx = _partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)
    return arr


def _partition(arr, low, high):
    pivot = arr[high]      # choose last element as pivot
    i = low - 1            # boundary of elements smaller than pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # put pivot in place
    return i + 1


# ==========================================================================================
# 6. HEAP SORT
# ==========================================================================================
# IDEA: Build a MAX-HEAP, repeatedly swap the root (largest) with the last element,
#       shrink the heap, and heapify the root back down.
#
# TIME : Best/Avg/Worst all O(n log n)
# SPACE: O(1)  | STABLE: No | IN-PLACE: Yes
#
# TRICK: "Build max-heap, pop the biggest to the back." Great when you need O(1) space
#        with guaranteed n log n. Parent of i = (i-1)//2, children = 2i+1 and 2i+2.
#
# DRY RUN on [5, 1, 4, 2]:
#   build max-heap -> [5,2,4,1]
#   swap root 5 with last -> [1,2,4,5] heapify [1,2,4] -> [4,2,1,5]
#   swap root 4 with last -> [1,2,4,5] heapify [1,2] -> [2,1,4,5]
#   swap root 2 -> [1,2,4,5]
#   RESULT: [1, 2, 4, 5]
def heap_sort(arr):
    n = len(arr)
    # build max-heap (start from last non-leaf node)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)
    # extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # move current max to the end
        _heapify(arr, i, 0)
    return arr


def _heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)


# ==========================================================================================
# 7. COUNTING SORT  (Non-Comparison)
# ==========================================================================================
# IDEA: Count occurrences of each value, then use the counts to place elements directly.
#       Works only for integers in a known, small range k.
#
# TIME : O(n + k)  | SPACE: O(k) | STABLE: Yes | IN-PLACE: No
#
# TRICK: "Count, accumulate, place." Beats n log n when k is small. Used inside Radix Sort.
#
# DRY RUN on [2, 5, 3, 0, 2, 3, 0, 3] (range 0..5):
#   counts   -> index: 0 1 2 3 4 5  ->  [2,0,2,3,0,1]
#   prefix   -> [2,2,4,7,7,8]  (positions)
#   place each element using prefix (right to left keeps stability)
#   RESULT: [0, 0, 2, 2, 3, 3, 3, 5]
def counting_sort(arr):
    if not arr:
        return arr
    min_val, max_val = min(arr), max(arr)
    range_size = max_val - min_val + 1
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1
    # prefix sums give final positions
    for i in range(1, range_size):
        count[i] += count[i - 1]
    output = [0] * len(arr)
    # iterate right-to-left to keep it STABLE
    for num in reversed(arr):
        count[num - min_val] -= 1
        output[count[num - min_val]] = num
    return output


# ==========================================================================================
# 8. RADIX SORT  (Non-Comparison)
# ==========================================================================================
# IDEA: Sort numbers digit by digit, from least significant digit (LSD) to most,
#       using a STABLE sub-sort (counting sort) at each digit.
#
# TIME : O(d * (n + k))  where d = number of digits, k = base (10)
# SPACE: O(n + k) | STABLE: Yes | IN-PLACE: No
#
# TRICK: "Sort by ones, then tens, then hundreds." Stability at each pass is essential.
#
# DRY RUN on [170, 45, 75, 90, 802, 24, 2, 66]:
#   by 1s   -> [170, 90, 802, 2, 24, 45, 75, 66]
#   by 10s  -> [802, 2, 24, 45, 66, 170, 75, 90]
#   by 100s -> [2, 24, 45, 66, 75, 90, 170, 802]
#   RESULT: [2, 24, 45, 66, 75, 90, 170, 802]
def radix_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    exp = 1  # current digit place (1, 10, 100, ...)
    while max_val // exp > 0:
        arr = _counting_sort_by_digit(arr, exp)
        exp *= 10
    return arr


def _counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # digits 0..9
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for num in reversed(arr):  # right-to-left keeps stability
        digit = (num // exp) % 10
        count[digit] -= 1
        output[count[digit]] = num
    return output


# ==========================================================================================
# 9. BUCKET SORT  (Non-Comparison / Distribution)
# ==========================================================================================
# IDEA: Distribute elements into several buckets, sort each bucket (often with insertion
#       sort), then concatenate. Best for uniformly distributed floating-point data in [0,1).
#
# TIME : Best/Avg O(n + k), Worst O(n^2) [all in one bucket]
# SPACE: O(n) | STABLE: Yes (if bucket sort is stable) | IN-PLACE: No
#
# TRICK: "Scatter into buckets, sort each, gather." Great for uniform real numbers.
#
# DRY RUN on [0.42, 0.32, 0.75, 0.12] with 4 buckets:
#   bucket index = int(val * n)
#   0.42->b1, 0.32->b1, 0.75->b3, 0.12->b0
#   b0=[0.12] b1=[0.42,0.32]->sort->[0.32,0.42] b3=[0.75]
#   concat -> [0.12, 0.32, 0.42, 0.75]
def bucket_sort(arr):
    if not arr:
        return arr
    n = len(arr)
    buckets = [[] for _ in range(n)]
    max_val = max(arr)
    for num in arr:
        # normalise so index stays within range (handles ints and floats)
        idx = int(n * num / (max_val + 1))
        buckets[idx].append(num)
    result = []
    for bucket in buckets:
        result.extend(insertion_sort(bucket))  # sort each bucket
    return result


# ==========================================================================================
#                                   DEMO / SELF-TEST
# ==========================================================================================
if __name__ == "__main__":
    sample = [5, 1, 4, 2, 8, 3, 7, 6]
    print("Original:        ", sample)
    print("Bubble Sort:     ", bubble_sort(sample.copy()))
    print("Selection Sort:  ", selection_sort(sample.copy()))
    print("Insertion Sort:  ", insertion_sort(sample.copy()))
    print("Merge Sort:      ", merge_sort(sample.copy()))
    print("Quick Sort:      ", quick_sort(sample.copy()))
    print("Heap Sort:       ", heap_sort(sample.copy()))
    print("Counting Sort:   ", counting_sort(sample.copy()))
    print("Radix Sort:      ", radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))
    print("Bucket Sort:     ", bucket_sort([0.42, 0.32, 0.75, 0.12, 0.68, 0.05]))

    # verify all comparison/integer sorts match Python's built-in
    expected = sorted(sample)
    for name, fn in [
        ("bubble", bubble_sort), ("selection", selection_sort),
        ("insertion", insertion_sort), ("merge", merge_sort),
        ("quick", quick_sort), ("heap", heap_sort), ("counting", counting_sort),
    ]:
        assert fn(sample.copy()) == expected, f"{name} FAILED"
    print("\nAll sorts verified correct against sorted():", expected)
