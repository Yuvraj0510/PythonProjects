r = int(input("ENTER A NUMBER :"))
v=0
while r>0:
    f= r%10
    v +=f
    r= r//10
print(v)
