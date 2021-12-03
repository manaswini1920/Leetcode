def sqrt(x):
    if x==0 or x==1:
        return x
    i=1
    res=1
    while res<=x:
        i+=1
        res=i*i

    return i-1
print(sqrt(11))

#approach 2 Newtons method
"""def mySqrt(self, x: int) -> int:
    if x == 0 or x == 1:
        return x
    x0 = x
    x1 = (x0 + x / x0) / 2
    while abs(x0 - x1) >= 1:
        x0 = x1
        x1 = (x0 + x / x0) / 2
        print(x0, x1)
    return int(x1)"""
