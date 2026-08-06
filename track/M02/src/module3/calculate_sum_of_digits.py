number=int(input("Enter a number: "))
sum_of_digits=0
while number > 0:
    digits=number%10
    sum_of_digits=digits+sum_of_digits
    number=number//10
print(f"sum of Digits: {sum_of_digits}")
