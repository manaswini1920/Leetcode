'''
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.
Example 1:

Input: s = "aab"
Output: 0
Explanation: s is already good.
'''


def minDeletions(s):
    # prepare a hashset
    d = dict()
    for i in s:
        if i not in d:
            d[i] = 0

        d[i] += 1
    # check
    count = 0
    vals = []
    for char in d:
        while d[char] in vals and d[char] > 0:
            count += 1
            d[char] -= 1
        vals.append(d[char])
    return count
print(minDeletions("aab"))