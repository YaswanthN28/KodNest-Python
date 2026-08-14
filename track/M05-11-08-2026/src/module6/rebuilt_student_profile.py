class StudentProfile:
    def __init__(
        self,
        student_id,
        name,
        course,
        experience,
        skills
    ):
    # Store all received values as instance attributes
        self.student_id=student_id,
        self. name=name,
        self.course=course,
        self. experience=experience,
        self.skills=skills

student_id = int(input("Enter a Student ID :"))
name = input("Enter a Name :").strip()
course = input("Enter a course :").strip()
experience = int(input("Enter a Experience in years :"))
skills = input("Enter a skills :").split()

# Create one StudentProfile object
StudentProfile=(student_id, name, course, experience, skills)
# Print the data stored in the object
print(f"Student ID: {student_id}")
print(f"Name: {name}")
print(f"Course: {course}")
print(f"Experience in Years: {experience}")
print(f"Skills: {', '.join(skills)}")
