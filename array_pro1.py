import array as arr
import numpy as np
x=arr.array('i',[]);
n=int(input("enter the no.of elements"));
for i in range(0,n):
      p=int(input("enter element"));
      x.append(p);
      
for i in range(n):
    for j in range(n):
        if(x[i]==2*x[j]):
            print(np.array([x[j],x[i]]));
                            
