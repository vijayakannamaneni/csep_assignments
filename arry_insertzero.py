import numpy as np
lst=list(map(int,input("\enter the number: ").strip().split()))
arr=np.array(lst)
i=0
while(i<len(arr)):
    if arr[i]==0:
        arr=np.insert(arr,i,0)
        i+=1
    i+=1
print(arr)
