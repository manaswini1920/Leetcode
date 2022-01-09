'''
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces.
Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"
'''
from collections import  deque
def reverse_words(s):
    #remove leading and trailing whitespaces
    i=0
    j=len(s)-1
    while i<=j and s[i]==' ':
        i+=1
    while i<=j and s[j]==' ':
        j-=1
    q=deque()
    word=[]
    while i<=j:
        if s[i]==' ' and word:
            q.appendleft(''.join(word))
            word=[]
        elif s[i]!=' ':
            word.append(s[i])
        i+=1
    #last iteration
    q.appendleft(''.join(word))
    return ' '.join(q)
print(reverse_words('the sky is blue    '))