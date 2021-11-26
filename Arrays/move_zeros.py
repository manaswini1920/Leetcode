def move_zeros(arr):
    i=0
    for j in range(len(arr)):
        if arr[j]!=0:
            arr[i]=arr[j]
            i+=1
    for j in range(i,len(arr)):
        arr[j]=0
    return arr
print(move_zeros([0,1,0,2,3]))

