m1= int(input("ENTER YOUR MARKS 1(OUT OF 100): "))
m2= int(input("ENTER YOUR MARKS 2(OUT OF 100): "))
m3= int(input("ENTER YOUR MARKS 3(OUT OF 100): "))
m4= int(input("ENTER YOUR MARKS 4(OUT OF 100): "))
m5= int(input("ENTER YOUR MARKS 5(OUT OF 100): "))
percentage= (m1+m2+m3+m4+m5)/5
if percentage>=95:
    print("YOUR GRADE IS A+")
elif 95>percentage>=90:
    print("YOUR GRADE IS A")
elif 90>percentage>=80:
    print("YOUR GRADE IS B")
elif 80>percentage>=70:
    print("YOUR GRADE IS C+")
elif 70>percentage>=60:
    print("YOUR GRADE IS C")
elif 60>percentage>=50:
    print("YOUR GRADE IS D")
else:
    print("YOUR GRADE IS F")


