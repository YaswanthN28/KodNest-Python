text=input("enter a character:")
count=0
for i in text:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count=count+1
print(f"number of vowels:{count}")