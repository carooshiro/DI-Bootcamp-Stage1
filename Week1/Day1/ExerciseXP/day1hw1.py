#Exercise1
print("Hello world\nHello world\nHello world\nHello world")

#Exercise2
print((99**3)*8)

#Exercise3

#False(5 < 3)
#True (3 == 3)
#False (3 == "3")
#Error ("3" > 3)
#False ("Hello" == "hello")

print(5 < 3)
print(3 == 3)
print(3 == "3")
#print("3"> 3)
print("Hello" == "hello")

#Exercise4
computer_brand = "hp"
print(f"I have a {computer_brand} computer.")

#Exercise5
name = "Carolina"
age = 44
shoe_size = 37

info = f"My name is {name}, I am {age} years old, and my shoe size is {shoe_size}."
print(info)

#Exercise6
a = 20
b = 17

if a > b:
    print("Hello World")

#Exercise7
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#Exercise8
my_name = "Carolina"

user_name = input("What is your name? ")

if user_name.lower() == my_name.lower():
    print("What?! We have the same name! Are you my twin? 😂")
else:
    print(f"Nice to meet you, {user_name}! Your name is different from mine! 😄")

#Exercise9
height = int(input("What is your height in centimeters? "))

if height > 145:
    print("You are tall enough to ride!")
else:
    print("You need to grow some more to ride.")
