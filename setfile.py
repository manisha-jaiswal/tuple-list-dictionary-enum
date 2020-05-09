#set is a collection of well defined object
s=set()
print(type(s))
s_from_list=set([1,2,3,4])
print(s_from_list)
print(type(s_from_list))

#ading elements
s.add(1)
#s.add(1) #it returns no output. bcoz set contains only uniques value. so here it returns only 1 time 1, but if we change the value then it returns , just check
s.add(2)
print(s)
s1=s.union({5,6,7})
print(s1)
s1.remove(5)
print(s1)
print(s.isdisjoint(s1))
print(s1,s)
s2=s.intersection(s,s1)
print(s2)
print(max(s1))
print(min(s1))
