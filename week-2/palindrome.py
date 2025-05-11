def is_palindrome(s):
    cleaned = s.lower().replace(" ", "").replace(",", "").replace(".", "")
    return cleaned == cleaned[::-1]

print(is_palindrome("madam"))   
print(is_palindrome("Hello"))   
