text = input("Enter a string: ")

if len(text) < 10:
    print("String not long enough.")
elif len(text) > 10:
    print("String too long.")
else:
    print("Perfect string")

    print("First character:", text[0])
    print("Last character:", text[-1])

    result = ""
    for char in text:
        result += char
        print(result)