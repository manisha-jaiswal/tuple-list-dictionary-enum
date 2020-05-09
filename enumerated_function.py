l1=["Bhindi","Aloo","Chowmin","Pasta"]
#there is a prbm.now u take only odd position saman,skip even position
#this is normal programming
i=1
for item in l1:
    if i%2 is not 0:
        print(f"Manisha please buy {item}")
    i+=1
#now we use enumareated
#here it starts from 0 so here we use even position
for index,item in enumerate(l1):
    if index %2==0:
        print(f"Sanu please bye {item}")

