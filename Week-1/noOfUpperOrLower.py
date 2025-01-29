def count_case(string):
    uppercase_count = 0
    lowercase_count = 0

    for char in string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    return uppercase_count, lowercase_count

user_string = input("Enter a string: ")

uppercase, lowercase = count_case(user_string)
print(f"Number of uppercase letters: {uppercase}")
print(f"Number of lowercase letters: {lowercase}")
