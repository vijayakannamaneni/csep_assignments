k=["chi","ich","hic","run","nur"];
dict={}
for i in k:
    key="".join(sorted(i))
    if key in dict.keys():
        dict[key].append(i);
    else:
        dict[key]=[]
        dict[key].append(i);
print(dict)
print(list(dict.values()))
print(list(dict.keys()))
