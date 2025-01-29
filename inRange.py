def is_in_range(number, start, end):
    return start <= number <= end

num = int(input("Enter the number to check: "))
range_start = int(input("Enter the start of the range: "))
range_end = int(input("Enter the end of the range: "))

if is_in_range(num, range_start, range_end):
    print(f"{num} is in the range [{range_start}, {range_end}].")
else:
    print(f"{num} is not in the range [{range_start}, {range_end}].")
