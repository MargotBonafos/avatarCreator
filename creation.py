from random import randint
import requests

def choose_random_string(file_name):
    with open(file_name, "r", encoding="utf8") as f:
        lines = f.readlines()
        line_choice = randint(0, len(lines) - 1)
        name = lines[line_choice].strip()
    return name

nameChoosen = choose_random_string("names_dictionnary.txt")
print(nameChoosen)

surnameChoosen = choose_random_string("surnames_dictionnary.txt")
print(surnameChoosen)


s = requests.Session()
s.headers.update({"User-Agent":"YourTool/1.0"})
r = s.get("https://exemple.com/api/items?limit=20")
r.raise_for_status()
print(r.json())