#dictionary is nothing but a key value pairs
d1={}  #dictionary is used curly braces
print(type(d1))
d2={"Harry":"Burger","Manisha":"Fish","Sanu":"Motton"}
print(d2)
print(d2["Harry"])
print(d2["Manisha"])
print(d2["Sanu"])
d3={"Manu":"Fish","Sanu":"Motton","Manisha":"Chicken Biryani","Avinash":{"B":"Maggi","L":"Roti","D":"Kheer"}}
print(d3)
print(d3["Avinash"]["D"])
d3["Ankit"]="Junk Food"
print(d3)
d3["Aurangjeb"]="Kababs"
print(d3)
d3["420"]="Muslim"
print(d3)

#delete
del d3["Aurangjeb"]
print(d3)

#Copy
d4=d3 #it is not copy the value from d3 , it indicate the d3
del d4["Manu"]
print(d3)

d4=d3.copy()
del d4["Sanu"]
print(d3)
print(d4)
#get function
print(d3.get("Sanu"))

#update function
d3.update({"Manu":"Chicken"})
print(d3)

#print all the keys value
print(d3.keys())
#print items
print(d3.items())#it print keys value as well as items
