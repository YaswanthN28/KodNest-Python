def calculate(first_number, second_number, operator):
    # Write your code here
    if operator == '+':
        return first_number + second_number
    elif operator == '-':
        return first_number - second_number
    elif operator == '**':
        return first_number * second_number
    elif operator == '/':
        return first_number / second_number
    else:
        return "Invalid operator"
first_number = int(input("enter a first number: "))
second_number = int(input("enter a second number: "))
operator = input("enter an operator: ").strip()

result = calculate(first_number, second_number, operator)
print(result)
