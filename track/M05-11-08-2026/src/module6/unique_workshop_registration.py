n = int(input("enter number of students: "))
registrations = set()

# Read and store the student IDs
for _ in range(n):
    student_id = input("enter the student id: ").strip()

registrations.add(student_id)
search_id = input("enter the student id to search: ").strip()
unique_count = 0
unique_count=len(registrations)
# TODO: Calculate the number of duplicate entries
duplicate_count = 0
duplicate_count=n - unique_count
# Print the counts
print(f"Unique registrations: {unique_count}")
print(f"Duplicate entries: {duplicate_count}")

if search_id in registrations:
    print("Registered")
else:
    print("Not Registered")