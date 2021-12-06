def intersection_of_two_arrays_ii(nums1,nums2):
    i=0
    j=0
    nums1=sorted(nums1)
    nums2=sorted(nums2)
    output=[]
    while i<len(nums1) and j<len(nums2):
        if nums1[i]>nums2[j]:
            j+=1
        elif nums1[i]<nums2[j]:
            i+=1
        else:
            output.append(nums1[i])
            i+=1
            j+=1
    return output
print(intersection_of_two_arrays_ii([4,9,5],[9,4,9,8,4]))