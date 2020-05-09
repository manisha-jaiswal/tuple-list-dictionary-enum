"""grocery=["HArpic","vim bar","deodrant","bhindi","lollypop",56] #mix list with string and integer
print(grocery)
print(grocery[0])
print(grocery[1])
print(grocery[5])
#print(grocery[6]) it gives error cause thre is maximum 5 items in a list
"""
numbers=[2,7,9,11,3]
print(numbers)
"""
print(numbers[2])
#slicing
print(numbers[0:5])
print(numbers[:5])
print(numbers[:])
print(numbers[1:])
print(numbers[1:4])
print(numbers)

#extended slice
print(numbers[::1])
print(numbers[::2])
print(numbers[::3])
print(numbers[::-1])
print(numbers[::-2])
print(numbers[::-3])
print(numbers[1:5:-3])
print(numbers[1:5:2])
print(len(numbers))
print(max(numbers))
print(min(numbers))

#Append
numbers.append(7)
numbers.append(17)
numbers.append(71)
print(numbers)

#insert
numbers.insert(1,67)
print(numbers)

#remove
numbers.remove(67)
print(numbers)

#pop
numbers.pop()
print(numbers)
numbers2=[]
numbers2.append(7)
numbers2.append(17)
numbers2.append(71)
print(numbers2)
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

"""

numbers[1]=98 #change the value fom index 1
print(numbers)


