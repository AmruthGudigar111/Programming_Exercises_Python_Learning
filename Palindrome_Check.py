text = "mom"
text1 = text[::-1]  # The slicing [::-1] reverses the string

# Check if the original string and the reversed string are the same
if text == text1:
    print("Your string is a palindrome")
else:
    print("Your string is not a palindrome")