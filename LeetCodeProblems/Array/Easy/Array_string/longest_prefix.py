"""
Problem: Longest Common Prefix
Link: https://leetcode.com/problems/longest-common-prefix/

Pattern:
- Vertical Scanning (Strings)

Idea:
- Take the first string as reference
- Compare its characters index-by-index with all other strings
- Stop when a mismatch or string length issue occurs
- Return the prefix found so far

Why this works?
- Any common prefix must be part of the first string
- Comparing column-wise ensures correctness

Time Complexity: O(n * m)
- n = number of strings
- m = length of the shortest string

Space Complexity: O(1)

Edge Cases:
- Empty input array
- One string only
- One string shorter than others
- No common prefix at all
"""

def longestCommonPrefix(strs):
    if not strs:
        return ""

    first = strs[0]

    for i in range(len(first)):
        for word in strs:
            if i >= len(word) or word[i] != first[i]:
                return first[:i]

    return first
