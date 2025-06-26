
s = input("Enter a string: ")
rev = s[::-1]

print("Reversed string:", rev)
if s == rev:
    print("Palindrome")
else:
    print("Not a palindrome")
