def get_element_at_index(numbers, index):
    try:
        element = numbers[index]
        print("Element at index", index, "is", element)
    except IndexError:
        print("Error: Index", index, "is out of range")

numbers = input("Enter a list (comma seperated):").split(",")
index = int(input("Enter the index: "))
get_element_at_index(numbers, index)
