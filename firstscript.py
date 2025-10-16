import sys                  # Load a library module
print(sys.platform)
print(2 ** 100)             # Raise 2 to a power
x = 'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."
print(x.title())

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
motorcycles.pop()
print(motorcycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
sortedCar =sorted(cars)
print(sortedCar)

print("\n blahhhhhhhhhhhhh")
magicians = ['alice', 'david', 'carolina']
for x in magicians:
        print(f"{x.title()} is a great car!")


for value in range(1, 6):
    print(value)

list2= list(range(1, 6))
print(list2)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

for number in range(10,1, -1):
    print(number)

#list comprehension
squares = [value**2 for value in range(1, 11)]
print(squares)

#list comprehension with condition
squares2 = [value/10 for value in range(12, 18) if (value % 2 == 1 and value >14) or value ==12]
print(squares2)

#slice of list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
print(players[:9])
print(players[6:])
print(players)

for player in players[:3]:
    print(player.title())


#coniditional statement in list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

age_0 = 22
age_1 = 18
if age_0 >= 21 or age_1 >= 21:
    print("At least one of you is 21 or older.")


game_active = True
can_edit = False

print(game_active and can_edit)


age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")


empty_list_check = []

if empty_list_check:
    for el in empty_list_check:
        print(f"Adding {el}.")
    print("\nFinished making your pizza!")
else:
    print("ListEmpty: We need to find some toppings!")


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")



#  Using the get() method to retrieve a value from a dictionary with a default value if the key does not exist.
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# Looping through a dictionary
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print(f"\nKeys: {key}")
    print(f"Value: {value}")

for user in user_0.values():
    print(f"keyssss {user.title()}")


# Defining a function
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username}!")

greet_user('jesse')


# Function with default argument and keyword argument, once you use keyword argument 
# you have to use it for all the rest of the arguments
# pet_name and animal_type arguments are keyword arguments and animal_type paramenter has a default value
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster',pet_name='willie')

describe_pet('mary')

#function_name(list_name[:]) to pass a copy of the list to the function

#to pass an arbitrary number of arguments use * before the paraemeter name
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)      
    
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)