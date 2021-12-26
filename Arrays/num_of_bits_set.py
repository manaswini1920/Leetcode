def count_of_bits(left,right):
    def is_prime(n):
        if n>1:
            for i in range(2,n):
                if n%i==0:
                    return False
            return True
    count=0
    for i in range(left,right+1):
        if is_prime(bin(i).count('1')):
            count+=1
    return count
print(count_of_bits(6,10))