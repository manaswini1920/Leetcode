"""
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Input: haystack = "", needle = ""
Output: 0
"""
def strstr(haystack,needle):
    if not needle or not haystack:
        return 0
    if len(haystack)<len(needle):
        return -1
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)]==needle:
            return i
    return -1
print(strstr("hello","ll"))