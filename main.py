import re

input = input("Enter a variable name: ")
keywords = ["False", "None", "True", "and", "as", "assert", "break", "class", "continue", "def", "del", "elif", "else", "except", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"]


if re.search(r'[@#$%^&*()\-_+=\[\]{}\\\|:;"\'<>,.?]', input):
    special_char = re.search(r'[@#$%^&*()\-_+=\[\]{}\\\|:;"\'<>,.?]', input).group()
    print(f"Invalid variable name. Variable names cannot contain special character '{special_char}'.")
elif input in keywords:
    print(f"Invalid variable name. Variable names cannot be Python keyword '{input}'.")
elif re.search(r'\s', input):
    print("Invalid variable name. Variable names cannot contain spaces.")
elif re.match(r'^\d', input):
    print("Invalid variable name. Variable names cannot start with a digit.")