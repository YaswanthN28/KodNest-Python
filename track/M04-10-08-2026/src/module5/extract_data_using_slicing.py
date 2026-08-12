word = input("enter a word: ")

first = int(input("enter first number: "))
second = int(input("enter second number: "))
third = int(input("enter third number: "))

numbers = [first, second, third]
record = (first, second, third)

# Slice the string, list and tuple
print("Middle:",word[1 :- 1])
print("First Two:", numbers [ : 2])
print("Reversed Tuple:", record [ : :- 1])