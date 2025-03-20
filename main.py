
animals = [
    {
        'name': 'Penguin',
        'group': 'Birds',
        'number_of_legs': 2,
        'skills': ['swimming', 'sliding on belly']
    },
    {
        'name': 'Kangaroo',
        'group': 'Mammals',
        'number_of_legs': 4,
        'skills': ['jumping', 'running']
    },
    {
        'name': 'Crocodile',
        'group': 'Reptiles',
        'number_of_legs': 4,
        'skills': ['swimming', 'hunting']
    },
    {
        'name': 'Bat',
        'group': 'Mammals',
        'number_of_legs': 2,
        'skills': ['flying', 'echolocation']
    },
    {
        'name': 'Octopus',
        'group': 'Mollusks',
        'number_of_legs': 8,
        'skills': ['swimming', 'camouflage', 'problem-solving']
    }
]

for animal in animals:
    print(f"{animal['name']} belongs to the group of {animal['group']} and has {animal['number_of_legs']} legs.")
    print(f"Skills: {', '.join(animal['skills'])}")
