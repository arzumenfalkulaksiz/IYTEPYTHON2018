text_1 = "Bu cumlede 4 elma 5 armut 8 tane de muz var"
x=text.replace("Bu","")
y=x.replace("cumlede","")
z=y.replace("elma","")
o=z.replace("armut","")
k=o.replace("tane","")
l=k.replace("de","")
m=l.replace("muz","")
n=m.replace("var","")
p=n.replace(" ","")
num1 = int(p)
text_2 = 'bu ikinci cumlede 9 kiraz 3 karpuz var'
a=text.replace("bu","")
b=a.replace("ikinci","")
c=b.replace("cumlede","")
d=c.replace("kiraz","")
e=d.replace("karpuz","")
f=e.replace("var","")
g=e.replace(" ","")
num2 = int(g)
print(num1)
print(num2)
print(num1+num2)
