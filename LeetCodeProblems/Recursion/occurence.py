# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Start small. Ship something.")



arr = [2, 4, 3, 4, 5, 6]
target = 4

def foccurence(arr, i, n, target):

    if i == n:
        return -1

    if arr[i] == target:
        return i

    return foccurence(arr, i + 1, n, target)

i = 0
n = len(arr)

first = foccurence(arr, i, n, target)
print("First occurrence of target", target, "is at index", first)

arr = [2, 4, 3, 4, 5, 6]
target = 4

def last_occurrence(arr, i, n, target):

    # Base case
    if i == n:
        return -1

    # Ask the rest of the array first
    ans = last_occurrence(arr, i + 1, n, target)

    # If the rest already found the target,
    # that's the last occurrence.
    if ans != -1:
        return ans

    # Otherwise, check the current element.
    if arr[i] == target:
        return i

    return -1
    
    
    
arr = [2, 4, 3, 4, 5, 4]
target = 4

def first_last_occurrence(arr, i, n, target):

    # Base case
    if i == n:
        return (-1, -1)

    # Get answer from the rest of the array
    first, last = first_last_occurrence(arr, i + 1, n, target)

    # Current element is the target
    if arr[i] == target:

        # If no occurrence was found ahead,
        # then current index is both first and last.
        if first == -1:
            return (i, i)

        # Otherwise, current index becomes the new first,
        # while the last remains unchanged.
        return (i, last)

    # Current element is not the target
    return (first, last)


first, last = first_last_occurrence(arr, 0, len(arr), target)

print("First occurrence :", first)
print("Last occurrence  :", last)
    


    