"""

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""
def reverse_str(word):
    i=0
    j=len(word)-1
    while i<j:
        temp=word[i]
        word[i]=word[j]
        word[j]=temp
        i+=1
        j-=1
    return word
print(reverse_str(['h','e','l','l','o']))