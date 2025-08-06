animals = [
    {"name": "Fluffy", "type": "dog"},
    {"name": "Parsley", "type": "dog"},
    {"name": "Ginger", "type": "cat"},
    {"name": "Biscuit", "type": "cat"},
    {"name": "Poppet", "type": "cow"}
]

def say_hello_to_pets(pets):
    for pet in pets:
        hello_message = ""
        pet_name = pet["name"]
        if pet["type"] == "dog":
            hello_message = "Woof"
        elif pet["type"] == "cat":
            hello_message = "Meow"
        else:
            raise Exception(pet["name"] + " is neither cat nor dog.")
        print(f"{hello_message}, {pet_name}!")

if __name__ == "__main__":
    say_hello_to_pets(animals)
