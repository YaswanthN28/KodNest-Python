# Read the course details
course_name=input("enter name: ")
current_week=input("enter current week: ")
course_status=input("enter course status: ")

# Create the original tuple
course_details=(course_name, current_week, course_status)

# Read the updated week
updated_week=input("enter updated week: ")

# Create and assign a new tuple
course_details=(course_details[0],updated_week, course_details[2])

# Display the updated tuple
print(course_details)