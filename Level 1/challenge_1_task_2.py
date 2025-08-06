name = input("What is your name? ")
if name.lower() == "alice" or name.lower() == "bob":
    print("Hello " + name.title() + "!")
else:
    print("Sorry... You're not authorised to be greeted!")
