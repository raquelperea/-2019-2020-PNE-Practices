import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-EX01.json").read_text()

# Create the object person from the json string
list_person = json.loads(jsonstring)

# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'

# Print the information on the console, in colors
print(f"Total people in the data base: {len(list_person)}")

for person in list_person:
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(person['Firstname'], person['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(person['age'])

    # Get the phoneNumber list
    phoneNumber = person['phoneNumber']

    # Print the number of elements in the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumber))

    # Print all the numbers
    for i, num in enumerate(phoneNumber):
        termcolor.cprint("  Phone {}:".format(i), 'blue')

        # The element num contains 2 fields: number and type
        termcolor.cprint("    Type: ", 'red', end='')
        print(num["type"])
        termcolor.cprint("    Number: ", 'red', end='')
        print(num["number"])