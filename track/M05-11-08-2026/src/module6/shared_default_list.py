def add_student(name, students=[]):
    students.append(name)
    print(students)

first_name = input("enter a name: ")
second_name = input("enter a name: ")
third_name = input("enter a name: ")

add_student(first_name)
add_student (second_name)
add_student (third_name)