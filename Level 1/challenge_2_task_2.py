import secrets

def reverse_name(name):
    return name[::-1]

def intersperse_name(forename, surname):
    username = ""
    for i in range(0, max(len(forename), len(surname))):
        try:
            username += reverse_name(forename)[i]
            username += surname[i]
        except:
            pass
    #print(username)
    return username

def format_name(name):
    new_name = name[:int(len(name)/2)] + " " + name[int(len(name)/2):]
    #print(new_name.capitalize())
    return new_name.title()

def generate_username():
    characters = "qwertyuiopasdfghjklzxcvbnm123456789"
    username = ''.join(secrets.choice(characters) for i in range(5)) + " " + ''.join(secrets.choice(characters) for i in range(5))
    return username

choice = input("Welcome to the username creator... Please choose one of the following options\n 1. Create a username based on a name\n 2. Generate a random username\n Enter your choice here: ")
if choice == "1":
    name = input("Enter your first name here: ")
    surname = input("Enter your surname here: ")
    username = intersperse_name(name, surname)
    print("Your username is: " + format_name(username))
else:
    print("Your username is: " + generate_username())