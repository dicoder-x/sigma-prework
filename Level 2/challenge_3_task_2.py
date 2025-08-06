directory = {'Jane': {'First name': "Jane",
                      'Last name': "Doe",
                      'Age': 42,
                      'Employed': True},
             'Tom': {'First name': "Tom",
                      'Last name': "Smith",
                      'Age': 18,
                      'Employed': True},
             'Mariam': {'First name': "Mariam",
                      'Last name': "Coulter",
                      'Age': 66,
                      'Employed': False},
             'Gregory': {'First name': "Gregory",
                      'Last name': "Tims",
                      'Age': 8,
                      'Employed': False}}

'''
Main directory key is the forename of each person to make accessing them using the list of names easier

TASK 1 is displayed before the TASK 2 main loop

Main loop has 3 commands:  add (add entry), remove (delete entry), exit (break loop)
Commands are NOT case sensitive

ADDING A PERSON REQUIRES THEIR FULL NAME OR ELSE EXCEPTION WILL BE THROWN 
e.g. "What is your name? (firstname lastname): " John -- INVALID
"What is your name? (firstname lastname): " efe743 3uyh4 -- VALID

'''

people = ['Jane', 'Tom', 'Mariam', 'Gregory']

def summary(person): # Return person entry in readable string
    return "Name: {} {}\nAge: {}\nEmployed: {}".format(directory[person]['First name'], directory[person]['Last name'], directory[person]['Age'], directory[person]['Employed'])
    
def add(): # Takes user input to add entry to dictionary & list
    try:
        name = input("What is your name? (firstname lastname): ")
        age = input("What is your age?: ")
        employee = input("Are you employed?: ")
        entry = {'First name': name.split()[0].title(), 'Last name': name.split()[1].title(), 'Age': int(age), 'Employed': True if employee.lower() == "yes" else False}
        directory[name.split()[0].title()] = entry
        people.append(name.split()[0].title())
    except:
        print("Invalid entry detected, please try again.")

def remove(): # Removes a dictionary & list entry if it exists
    person = input("Who is to be removed?: ").title()
    if person in people:
        directory.pop(person)
        people.remove(person)
        print("Removed " + person)
    else:
        print(person + " not in list")
    print(people)
    
### Main loop
for person in people:
    print(summary(person))

while True: # Loop until "exit" command
    choice = input("Type add to add a new entry or remove to delete an entry. Exit to break the loop.\n") # User input
    if choice.lower() == "exit":
        break
    elif choice.lower() == "add":
        add()
    elif choice.lower() == "remove":
        remove()
    else:
        print("Not a valid option!")