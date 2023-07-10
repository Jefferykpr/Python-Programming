def is_subset(set_a, set_b):
    return all(elem in set_b for elem in set_a)

a = set(input("enter a set1:"))
b = set(input("enter a set 2:"))
check = is_subset(b, a)
print(check)
