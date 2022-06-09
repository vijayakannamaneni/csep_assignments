import array as arr
a=arr.array('i',[1,2,3,4,5]);
high=len(a)-1;
low=0;

x=int(input("enter the  number u want to search"));
for i  in range(0,len(a)+1):
	mid=(low+high)//2;
	if(a[mid]>x):
		high=mid-1;
	elif(a[mid]<x):
		low=mid+1;
	
print("element found at:",i);

		

#by using while loop 
def bs(arr,x):
    low=0
    high=len(arr)-1
    mid=0
    while low<=high:
        mid=(high+low)//2
        if arr[mid]<x :
            low=mid+1
        elif arr[mid]>x :
            high=mid-1
        else :
            return mid
    return -1
