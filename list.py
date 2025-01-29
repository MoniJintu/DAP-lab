def get_unique_elements(input_list):
    unique_list = list(set(input_list))
    return unique_list

user_list = input("Enter a list of elements : ").split()
unique_list = get_unique_elements(user_list)
print("Unique elements:", unique_list)
