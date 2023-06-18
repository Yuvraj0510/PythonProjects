y=int(input("Classes held: "))
x=int(input("Classes attended: "))
print("Attendance percentage : ", (x*100)/y,"%")
if((x*100)/y<75):
    print("Not allowed to sit in exam")
else:
    print("Allowed to sit in exam")
