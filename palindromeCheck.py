def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam")) 
print(is_palindrome("hello"))  




def is_palindrome(s):
    return s == "".join(reversed(s))

print(is_palindrome("MAM"))  
print(is_palindrome("NOON"))  