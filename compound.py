def compound(p,rate,year):
    if year<=0:

        return p
    else:
        return compound(p+p*rate/100,rate,year-1)
amount=int(input("enter prinicipal amount"))
r=int(input("enter rate of intereet"))
y=int(input("enter no.of years"))
print("the compound interset is" ,compound(amount,r,y) )
