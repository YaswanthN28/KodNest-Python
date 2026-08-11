def check_eligibility(marks, attendance, project_completed):
    if marks>=60 and attendance>=75 and project_completed == "yes":
        return "Eligible"
    else:
        return "Not Eligible"

# Read the student's details
marks = int(input("enter marks: "))
attendance = int(input("enter attendance: "))
project_completed = input("enter project completed: ")


result = check_eligibility(marks, attendance, project_completed)
print(result)