#Mutable-can change
#immutable=cannot change
#tuples
tp=(1,2,3) #tuples are write in parenthesis
print(tp)
#tp[1]=8 - tuples values are immutable , it never change but list value are mutable , they are change
tp=(1)#it is not shown like tuple . so if want to define 1 single walue in touple , we use (,) after the first dentence

tp=(1,)
print(tp)

#swapping two numbers
a=1
b=8
a,b=b,a
print(a,b)