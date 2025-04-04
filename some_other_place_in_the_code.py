from names import get_random_name
from person import Person

persons = [
    {
        "name": get_random_name(),
        "hobbies": [
            "football",
            "racewarkingdoms mmorpg"
        ]
    },
    {
        "name": get_random_name(),
        "hobbies": [
            "cards",
            "drift cars"
        ]
    }
]

# print(persons[0])
# for hobby in persons[0]["hobbies"]:
#     print(hobby)

# print("======")
# # Make a persons list with at least 2 dictionaries representing a person with hobbies - DONE


# # create a function to print out the name of the persons

# for person in persons:
#     print(person['name'])

# print("======")
# # create a function to print out all hobbies of the persons eg. print(all_hobbies()) => ['tennis', 'working out', 'maths']
# hobbies_list = []

# for person in persons:
#     for hobby in person['hobbies']:
#         hobbies_list.append(hobby)

# print(hobbies_list)
# print("======")

person = Person('Jamie', ['cycling', 'making special coffees'])

print(person.print_hobbies())
print(person.print_name())