#Approach 1 --> recursion
def recfib(n):
    if n<=1:
        return n
    return recfib(n-1)+recfib(n-2)
#print(recfib(4))
#Approach 2 :memoization
def memofib(n):
    cache={0:0,1:1}
    if n in cache:
        return cache[n]
    cache[n]=memofib(n-1)+memofib(n-2)
    return cache[n]
#print(memofib(4))
#Approach 3: bottom up iterative method
def iterfib(n):
    if n <=1:
        return n
    temp=0
    n1=1
    n2=0
    for i in range(2,n+1):
        temp=n1+n2
        n2=n1
        n1=temp
    return temp
print(iterfib(4))