### PROMPT ###
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically
#using all the original letters exactly once.

### CONSTRAINTS ###
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.


import itertools
strs = ["eat","tea","tan","ate","nat","bat"] #input
sortstrs = strs.copy()
for i in range(len(strs)):
    sortstrs[i] = sorted(strs[i])

    print(sortstrs)

out = [[]]
out[0].insert(1,strs[1])
print(out)
for i in range(len(sortstrs)):
    print(type(sortstrs[i]))
    for j in range(i+1, len(sortstrs)):
        if sortstrs[i] == sortstrs[j]:
            out[i].insert(j,strs[j])
print(out)


## DEBUGGING ##
# print(strs[0])
# print(sorted(strs[0]))