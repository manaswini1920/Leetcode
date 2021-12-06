def reverse_words_iii(s):
    l,r=0,0
    res=''
    while r>len(s):
        if s[r]!=' ':
            r+=1
        elif s[r]==" ":
            res+=s[l:r+1][::-1]
            r+=1
            l=r
    res+=" "
    res+=s[l:][::-1]
    return res[1:] #because of whitespace in front
print(reverse_words_iii('ab cd'))