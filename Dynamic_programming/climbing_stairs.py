def climbing_stairs(n): #O(n), O(1)
    if n<=2:
        return n
    prev1=1
    prev2=2
    curr=0
    for i in range(2,n):
        curr=prev1+prev2
        prev1=prev2
        prev2=curr
    return curr
print(climbing_stairs(7))

#approach 2 => using formula O(logn),o(1)
'''
 public int climbStairs(int n) {
        double sqrt5=Math.sqrt(5);
        double fibn=Math.pow((1+sqrt5)/2,n+1)-Math.pow((1-sqrt5)/2,n+1);
        return (int)(fibn/sqrt5);
'''