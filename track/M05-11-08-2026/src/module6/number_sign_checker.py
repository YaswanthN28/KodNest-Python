def check_sign(number) :
    # Write your code .here
    if number > 0:
        return "Positive"
    elif number <0:
        return "Negative"
    elif number == 0:
        return "Zero"
number = int(input("enter a number: "))
result = check_sign (number)
print(result)