name = input("enter name: ")
course = input("enter course: ")
score = int(input("enter score: "))

# Create the tuple
student_record =(name, course, score)

# Unpack the tuple
name, course, score = student_record
# Display the unpacked values
print("Name:", name)
print("Course:", course)
print("Score:", score)