from my_array import Array

a = Array()
a.append(10)
a.append(20)
a.insert(1, 15)
print(a) 

a.remove(15)
print(a) 

popped = a.pop()
print(popped)  
print(a)      

