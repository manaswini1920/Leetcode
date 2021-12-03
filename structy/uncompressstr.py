"""
Write a function, uncompress, that takes in a string as an argument.
The input string will be formatted into multiple groups according to the following pattern:
<number><char>

for example, '2c' or '3a'.
The function should return an uncompressed version of the string where each 'char' of
a group is repeated 'number' times consecutively. You may assume that the input string is well-formed
according to the previously mentioned pattern.
test_00:
uncompress("2c3a1t") # -> 'ccaaat'
test_01:
uncompress("4s2b") # -> 'ssssbb'
test_02:
uncompress("2p1o5p") # -> 'ppoppppp'
"""
def uncompress(s):
    number='0123456789'
    i=0
    j=0
    res =[]
    while j<len(s):
        if s[j] in number:
            j+=1
        else:
            num=int(s[i:j])
            res.append(s[j]*num)
            j+=1
            i=j
    return ''.join(res)
print(uncompress('2a3b'))