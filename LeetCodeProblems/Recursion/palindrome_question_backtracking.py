'''
Problem
  
Palindromic Decomposition Of A String
Find all palindromic decompositions of a given string s.

A palindromic decomposition of string is a decomposition of the string into substrings, such that all those substrings are valid palindromes.

Example
{
"s": "abracadabra"
}
Output:

["a|b|r|a|c|ada|b|r|a", "a|b|r|aca|d|a|b|r|a", "a|b|r|a|c|a|d|a|b|r|a"]
Notes
Any string is its own substring.
Output should include ALL possible palindromic decompositions of the given string.
Order of decompositions in the output does not matter.
To separate substrings in the decomposed string, use | as a separator.
Order of characters in a decomposition must remain the same as in the given string. For example, for s = "ab", return ["a|b"] and not ["b|a"].
Strings in the output must not contain whitespace. For example, ["a |b"] or ["a| b"] is incorrect.
Constraints:

1 <= length of s <= 20
s only contains lowercase English letters.


'''

def generate_palindromic_decompositions(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    result = []
    path = []

    def is_palindrome(left, right):
        # check palindrome using two pointers
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def backtrack(start):
        # base case: reached end of string
        if start == len(s):
            result.append("|".join(path))
            return

        # try all possible partitions
        for end in range(start, len(s)):
            if is_palindrome(start, end):
                # choose
                path.append(s[start:end + 1])

                # explore
                backtrack(end + 1)

                # backtrack
                path.pop()

    backtrack(0)
    return result
"same code for palindrome partion"

def palindrome_partition(s):
    result = []
    path = []

    def is_palindrome(left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    def backtrack(start):

        # Base case
        if start == len(s):
            result.append(path.copy())
            return

        # Try every possible substring
        for end in range(start, len(s)):

            # Check if substring is palindrome
            if is_palindrome(start, end):

                # Choose
                path.append(s[start:end + 1])

                # Explore
                backtrack(end + 1)

                # Backtrack
                path.pop()

    backtrack(0)

    return result


