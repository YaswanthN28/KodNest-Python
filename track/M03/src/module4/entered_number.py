number_count=int(input("enter the number_count:"))
positive_count=0
negative_count=0
zero_count=0
total=0
for i in range (number_count):
    num=int(input())
    if num >0:
        positive_count+=1
        total+=num
    elif num<0:
        negative_count+=1
        total+=num
    elif num == 0:
        zero_count+=1
        total+=num
print("Positive Count:", positive_count)
print("Negative Count:", negative_count)
print("Zero Count:", zero_count)
print("Total:", total)