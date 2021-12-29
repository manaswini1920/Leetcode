def sort_colors(arr): #dutch national flag problem- three pointer approach
    p0,curr=0,0
    last=len(arr)-1
    while curr<=last:
        if arr[curr]==2:
            arr[curr],arr[last]=arr[last],arr[curr]
            last-=1
        elif arr[curr]==0:
            arr[p0],arr[curr]=arr[curr],arr[p0]
            curr+=1
            p0+=1
        else:
            curr+=1
    return arr
print(sort_colors([2,0,1,0,1]))