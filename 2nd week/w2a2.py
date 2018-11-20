import random
values = list(range(10))
a=random.choice(values)
a=int(a)
print a
b=random.choice(values)
b=int(b)
print b
secenek=random.choice(values)
secenek=int(secenek)
print secenek 
if (secenek==int(0)) :
   print (a+b)
else:
   print('Boyle bir secenek yok.')
