str="run"
str1=input("enter input string")
dic={}
dic1={}
for i in str:
    c=str.count(i)
    if i not in dic:
        dic[i]=c;
print(dic)
for k in str1:
    r=str.count(k)
    if k not in dic1:
        dic1[k]=r;
print(dic1)
if dic.items()==dic1.items():
    print("the given string is anagram")
else:
    print("not an anagram")

