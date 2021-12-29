import collections


def can_construct(ransomNote,magazine):
    if len(ransomNote)>len(magazine):
        return False
    letters=collections.Counter(magazine)
    for c in ransomNote:
        if letters[c]<=0:
            return False
        letters[c]-=1
    return True
print(can_construct('aa','a'))