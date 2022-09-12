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