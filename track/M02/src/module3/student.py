marks=int(input("enter marks:"))
if marks >= 90 and marks < 100:
    print("Grade is A")
elif marks >= 75 and marks < 89:
    print("Grade is B")
elif marks >= 60 and marks < 74:
    print("Grade is C")
elif marks >= 40 and marks < 59:
    print("Grade is D")
elif marks >= 0 and marks < 39:
    print("Grade is F")
else:
    print("Invalid Marks")