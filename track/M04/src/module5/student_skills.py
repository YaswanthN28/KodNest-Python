skills = []

# Read and store five skills
for i in range (5):
    skills.append(input("enter a skill: "))

# Convert the list into a tuple
tup=tuple(skills)

# Create the required slices
first=tup[0:3]
second=tup[3:]
alternate=tup[0: :2]
required=tup[ : :- 1]
# Display all required results
print(f"Skill Record: {tup}")
print(f"First Three: {first}")
print(f"Last Two: {second}")
print(f"Alternate Skills: {alternate}")
print(f"Reversed Skills: {required}")