from names import get_random_name
from person import Person

persons = [
    {
        "name": 'Hannah',
        "hobbies": [
            "tennis",
            "Warcraft 3"
        ]
    },
    {
        "name": 'Xiao',
        "hobbies": [
            "reading",
            "collecting diecast cars"
        ]
    }
]

# print(persons[0])
# for hobby in persons[0]["hobbies"]:
#     print(hobby)

# Make a persons list with at least 2 dictionaries representing a person with hobbies - DONE

# create a function to print out the name of the persons
# for person in persons:
#     print(person['name'])
# create a function to print out all hobbies of the persons eg. print(all_hobbies()) => ['tennis', 'working out', 'maths']

# hobbies_list = []

# for person in persons:
#     for hobby in person['hobbies']:
#         hobbies_list.append(hobby)

# print(hobbies_list)




person_1 = Person(get_random_name(), ['walking', 'learning about flowers'])

person_2 = Person(get_random_name(), ['reading', 'tennis'])

persons_list = [person_2, person_1]

for person in persons_list:
    print(person.name)

print("====")

hobbies_list = []

for person in persons_list:
    person.print_hobbies()
