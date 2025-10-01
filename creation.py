from random import randint

def choose_random_string(file_name):
    with open(file_name, "r", encoding="utf8") as f:
        lines = f.readlines()
        line_choice = randint(0, len(lines) - 1)
        name = lines[line_choice].strip()
    return name

nameChoosen = choose_random_string("names_dictionnary.txt")
print(nameChoosen)

