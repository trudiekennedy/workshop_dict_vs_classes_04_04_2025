from toy import Toy

toys = [
    {
        "name": "Ball",
        "colour": "red"
    },
    {
        "name": "Teddy",
        "colour": "brown"
    }
]

# Make a toys list with at least 2 dictionaries representing a toy with name and colour DONE

# create a function to print out the name of all toys
def toy_names(dict):
    for toy in dict:
        print(toy['name'])

# create a function to print out all colours of toys. print(print_colours()) => ['red', 'green']
def toy_colours(dict):
    for toy in dict:
        print(toy['colour'])

# Now do this with classes
toy_box = Toy(toys)
toy_box.return_name()
toy_box.return_colour()
