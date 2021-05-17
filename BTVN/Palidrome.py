def is_palindrome(string):
    string = str(string)
    if string == string[::-1]:
        return True
    return False

print(is_palindrome("21"))

