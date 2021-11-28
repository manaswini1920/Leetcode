"""
Given two binary strings a and b, return their sum as a binary string.
Example 1:
Input: a = "11", b = "1"
Output: "100"
Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""
def add_binary(a,b):
    carry=0
    res=""
    a,b=list(a),list(b)
    while a or b or carry:
        if a:
            carry+=int(a.pop())
        if b:
            carry+=int(b.pop())
        res+=str(carry%2)
        carry=carry//2
    return res[::-1]
print(add_binary("11","1"))