'''
The only scenario left is where isBadVersion(mid) \Rightarrow trueisBadVersion(mid)⇒true. This tells us
that midmid may or may not be the first bad version, but we can tell for sure that all versions after midmid can be discarded.
Therefore we set right = midright=mid as the new search space of interval [left,mid][left,mid] (inclusive).
In our case, we indicate leftleft and rightright as the boundary of our search space (both inclusive).
This is why we initialize left = 1left=1 and right = nright=n. How about the terminating condition?
 We could guess that leftleft and rightright eventually both meet and it must be the first bad version,
  but how could you tell for sure?The formal way is to prove by induction, which you can read up yourself if
   you are interested. Here is a helpful tip to quickly prove the correctness of your binary search algorithm
   during an interview. We just need to test an input of size 2. Check if it reduces the search space
    to a single element (which must be the answer) for both of the scenarios above. If not, your algorithm will never terminate.
If you are setting mid = \frac{left + right}{2}
mid= (left+right )/2
you have to be very careful. Unless you are using a language that does not overflow such as Python,
left + right could overflow. One way to fix this is to use left + (right-left)/2
  instead.
'''

def isBadVersion(n):
    pass # input is differently given
def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    left = 1
    right = n
    while left < right:
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left
'''
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
'''