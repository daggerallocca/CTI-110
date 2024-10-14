# Alana Allocca
# 10/2/2024
# P5HW
# Using AI and functions to create a game

#define a function to create a character
def create_character():
    name = input("Enter character name: ")
    
    # Get user input for health, atk, and def
    health = int(input("Enter health (recommended 50-100): "))
    atk = int(input("Enter attack (recommended 5-20): "))
    def_ = int(input("Enter defense (recommended 3-15): "))
    print()

    character = {
        "name": name,
        "health": health,
        "atk": atk,
        "def": def_,
        "is_alive": True
    }
    
    return character

def display_character(char):
    for key in list(char.keys())[:4]:  #Get the first 4 keys by slicing the dictionaries
        print(f"{key}: {char[key]}")

def is_alive(char):
    return char["health"] > 0

def attack(attacker, defender):
    if not is_alive(attacker):
        print(f"{attacker['name']} cannot attack because they are defeated!")
        return attacker, defender

    damage_dealt = attacker["atk"]
    defender["health"] -= damage_dealt
    print(f"{attacker['name']} attacks {defender['name']} for {damage_dealt} damage!")
    
    if defender["health"] <= 0:
        defender["health"] = 0
        defender["is_alive"] = False
        print(f"{defender['name']} has been defeated!")
    else:
        print(f"{defender['name']} has {defender['health']} health remaining.")
    
    return attacker, defender  # Return the updated dictionaries


def main():
    char1 = create_character()
    print()
    char2 = create_character()

    # Create a list
    char_list = [char1, char2]

    # Print one character's attributes
    display_character(char1)
    print("-*- vs. -*-")
    display_character(char2)

    # Call the attack function
    print()
    print("Begin!")
    print()
    char1, char2 = attack(char1, char2)

    # Display the updated characters
    display_character(char1)
    print()
    display_character(char2)

if __name__ == "__main__":
    main()
