marks=int(input("Enter marks: "))
attendance=int(input("Enter attendance: "))
status=input("Enter status: ")
if marks>=60 and attendance>=75:
    if status == "yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")