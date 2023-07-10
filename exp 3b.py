num = int(input("Enter the number of elements in the list: "))
list1 = []

for i in range(num):
    v = int(input("Enter the value: "))
    list1.append(v)

print("Original list:", list1)

ascending = True

for i in range(1, num):
    if list1[i] < list1[i-1]:
        ascending = False
        break
if ascending:
    print("Yes, the list is in ascending order.")
else:
    print("No, the list is not in ascending order.")
