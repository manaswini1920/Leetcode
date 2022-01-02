def max_subarray_sum(num):
    a=b=num[0]
    for i in num[1:]:
        print('a',a)
        a=max(a,a+i)

        b=max(a,b)
        print('b',b)
    return b
print(max_subarray_sum([-2,1,3,0]))
