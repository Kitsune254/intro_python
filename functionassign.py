def palindrome(a_string):
    a_string = a_string.lower().replace(' ', '')
    return a_string == a_string[::-1]


input_string = 'Was it a car or a cat I saw'
print(palindrome(input_string))

input_string = 'is this it'
print(palindrome(input_string))


word = input("Enter your word:")
if word == word[::-1]:
    print("It's a palindrome")
else:
    print("It's a not a palindrome")


string_to_check = input("Enter your string:")
if string_to_check == string_to_check[::-1]:
    print("This is a palindrome")
else:
    print("This is a not a palindrome")
