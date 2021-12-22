'''
Given a string s, reverse the string according to the following rules:
All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.
Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:
'''


def reverseOnlyLetters(s):
    s = list(s)
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i].isalpha() and s[j].isalpha():
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        elif s[i].isalpha() and not s[j].isalpha():
            j -= 1
        elif s[j].isalpha() and not s[i].isalpha():
            i += 1
        else:
            i += 1
            j -= 1
    return ''.join(s)
print(reverseOnlyLetters('ab-cd'))