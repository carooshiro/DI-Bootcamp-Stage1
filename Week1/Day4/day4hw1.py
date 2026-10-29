#Exercise1

my_fav_numbers = {3, 7, 10, 21}

my_fav_numbers.add(15)
my_fav_numbers.add(25)

my_fav_numbers.remove(25)

friend_fav_numbers = {7, 12, 18, 30}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(my_fav_numbers)
print(friend_fav_numbers)
print(our_fav_numbers)

#Exercise2

numbers = (1, 2, 3, 4)

# Tuples cannot be modified directly.
# numbers.append(5)  # This would cause an error.

numbers = numbers + (5, 6)

print(numbers)

#Exercise3

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")

basket.append("Kiwi")
basket.insert(0, "Apples")

print(basket.count("Apples"))

basket.clear()

print(basket)

#Exercise4

#A float is a number that has a decimal point. An integer (int) is a whole number without a decimal point

numbers = []

for i in range(3, 11):
    numbers.append(i / 2)

print(numbers)

#Exercise5

for number in range(1, 21):
    print(number)
for number in range(1, 21):
    if number % 2 == 0:
        print(number)

#Exercise6

while True:
    name = input("Enter your name: ")

    if len(name) >= 3 and not name.isdigit():
        print("Thank you")
        break
    else:
        print("Incorrect input. Please try again.")

#Exercise7

favorite_fruits = input("Enter your favorite fruits, separated by spaces: "
).lower().split()

fruit = input("Enter a fruit: ").lower()

if fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

#Exercise8

toppings = []

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")

    if topping.lower() == "quit":
        break

    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

total_cost = 10 + len(toppings) * 2.50

#Exercise9

ages = []
total_cost = 0

number_of_people = int(input("How many people are in your family? "))

for i in range(number_of_people):
    age = int(input("Enter the person's age: "))
    ages.append(age)

    if age < 3:
        total_cost += 0
    elif age <= 12:
        total_cost += 10
    else:
        total_cost += 15

print(f"Total ticket cost: ${total_cost}")

#Bonus

ages = [15, 16, 18, 22, 20, 14, 21]

i = 0

while i < len(ages):
    if ages[i] < 16 or ages[i] > 21:
        ages.pop(i)
    else:
        i += 1

print("Final list of attendees:", ages)
