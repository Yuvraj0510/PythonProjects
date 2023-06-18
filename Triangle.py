a=int(input("Length of 1st side:"))
b=int(input("Length of 2nd side:"))
c=int(input("Length of 3rd side:"))
if(a==b==c):
    print(" Triangle is Equilateral triangle")
elif(a!=b==c):
    print("Triangle is isoceles")
elif(a==b!=c):
    print("Triangle is isoceles")
elif(a==c!=b):
    print("Triangle is isoceles ")
else :
    print("Triangle is Scalene ")

