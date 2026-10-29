text = input("Enter a string: ")

if len(text) < 10:
    print("String not long enough.")
elif len(text) > 10:
    print("String too long.")
else:
    print("Perfect string")

    print("First character:", text[0])
    print("Last character:", text[-1])

result = "" #creates an empty string where we store the characters one by one as the loop runs
i = 0

while i < len(text): #The while loop adds one character at a time to result and increases i until all characters in text have been added
    result += text[i]
    print(result)
    i += 1