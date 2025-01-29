def find_largest_item(input_list):
    if not input_list: 
        return "The list is empty."
    return max(input_list)

user_list = list(map(int, input("Enter a list of numbers: ").split()))

largest_item = find_largest_item(user_list)
print("The largest item in the list is:", largest_item)
