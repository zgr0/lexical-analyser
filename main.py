input = input("Enter a variable name: ")
special =["@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", "|", "\\", ":", ";", "\"", "'", "<", ">", ",", ".", "?"]
keywords = ["False", "None", "True", "and", "as", "assert", "break", "class", "continue", "def", "del", "elif", "else", "except", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"]
for i in input:
    if i in special:
        print(f"Invalid variable name. Variable names cannot contain special character '{i}'.")
        break
if input in keywords:
    print(f"Invalid variable name. Variable names cannot be Python keyword '{input}'.")

if " " in input:
    print("Invalid variable name. Variable names cannot contain spaces.")

if input[0].isdigit():
    print("Invalid variable name. Variable names cannot start with a digit.")