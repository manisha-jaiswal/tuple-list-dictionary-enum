#numbers=["3","34","64"]
"""
for i in range(len(numbers)):
    numbers[i]=int(numbers[i])
numbers[2]=numbers[2]+1
print(numbers[2])
"""
#it is very lengthy
#so here we use map , for loop ki jgh pr
"""numbers=list(map(int,numbers))
numbers[2]=numbers[2]+1
def sq(a):
    return a*a
num=[2,3,4,5,6,7]
square=list(map(sq,num))
square=list(map(lambda x: x*x , num))
print(square)
"""
"""
#---------------------------------MAP------------------------------------
def square(a):
    return a*a
def cube(a):
    return a*a*a
func=[square,cube]
for i in range(5):
    val=list(map(lambda x:x(i),func))
    print(val)
"""
"""
#----------------------------------------FILTER-----------------------------
list1=[1,2,3,4,5,6,8,9,55,66,42,25]
def is_greater_5(num):
    return num>5
gr_than_5=list(filter(is_greater_5,list1)) #filter function aisi list bnata h elements ki jo true return krta h
print(gr_than_5)
"""
#-----------------------------REDUCE-----------------------------------------
from functools import reduce #reduce is a part of functools module
list3=[1,2,3,4]
num= reduce(lambda x,y:x+y,list3)
num1=reduce(lambda x,y:x*y,list3)
print(num)
print(num1)


