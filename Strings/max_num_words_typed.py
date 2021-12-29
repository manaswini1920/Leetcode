def max_num_of_words_can_type(s,brokenletters):
    res=0
    for i in s.split():
        valid=True
        for j in set(brokenletters):
            if j in i:
                valid=False
                break
        if valid:
            res+=1
    return res
print(max_num_of_words_can_type("hello world",''))


