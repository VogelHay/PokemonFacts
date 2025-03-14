'''
https://www.youtube.com/watch?v=JVQNywo4AbU
Youtube link for tutorial

pip install requests = how to install mods, in this instance "requests"
'''

import requests
import sys

base_url = "https://pokeapi.co/api/v2/"

# Reset API request
def reset_pokemon_info():
    reset = input("Would you like to try again? (y/n) ")
    if reset == 'y':
        main()
    elif reset == 'n':
        sys.exit()
    else:
        print("Unrecognized syntax! Please try again." )
        reset_pokemon_info()

# Function to pull info from Pokemon API
def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        poke_data = response.json()
        return poke_data
    elif response.status_code == 404:
        reset_pokemon_info()
    else:
        main()

#Writes to pokemon_file to store user information
def pokemon_file():
    if poke_info:
        info = open("pokemon_info.txt", "w")
        info.write(f"{poke_dict}")

        info = open("pokemon_info.txt", "r")
        return info

# Manually looks up requests 
def pokemon_lookup():
    if poke_info:
        key = input('''Please choose a category to declare:
(Type in all lowercase, type 'help' for a list of all commands.
To input multiple categories, seperate each key with ', ' ) ''')
        dict_keys = [poke_dict.keys()]
        res = any(x == key for x in dict_keys)

        if key == 'help':
            print(poke_dict.keys())
            input('Press enter to continue')
            pokemon_lookup()
        elif key == res:
            print(f"{poke_info[key]}")
        else:
            print("Unrecognized syntax! Please try again." )
            pokemon_lookup()

# Lookup user input on API and creates a file to store info.
# Also creates a dictionary value for lookup function
def main():
    global poke_name
    global poke_info
    global poke_dict

    poke_name = input("Name a pokemon (use all lowercase please): ")
    poke_info = str(get_pokemon_info(poke_name))
    poke_dict = {i.split(':')[0]: str(i.split(':')[1]) for i in poke_info.split(", ")}
#   Need to figure out how to split the dict into smaller subdicts to store categories
    print(poke_info)

    pokemon_file()
    pokemon_lookup()

# PROGRAM BEGINS HERE
main()
