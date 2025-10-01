from random import randint
import requests
from pathlib import Path

def choose_random_string(file_name):
    with open(file_name, "r", encoding="utf8") as f:
        lines = f.readlines()
        line_choice = randint(0, len(lines) - 1)
        name = lines[line_choice].strip()
    return name

def create_folder(completeName ):
    out_dir = Path(f"results/{completeName}")
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir


def insert_photo_in_folder(dir, img):

    file_name = f"{dir.name}_photo.png" 

    (dir / file_name).write_bytes(img)


def thisPersonDoesNotExist_request():
    s = requests.Session()
    s.headers.update({"User-Agent":"YourTool/1.0"})
    r = s.get("https://thispersondoesnotexist.com/")
    r.raise_for_status()

    print("Content-Type:", r.headers.get("Content-Type"))

    img = r.content
    #with open("favicon.ico", "wb") as f:
    #    f.write(img)

    return img


nameChoosen = choose_random_string("names_dictionnary.txt")
print(nameChoosen)

surnameChoosen = choose_random_string("surnames_dictionnary.txt")
print(surnameChoosen)

image_getted = thisPersonDoesNotExist_request()

new_dir = create_folder(f"{nameChoosen}_{surnameChoosen}")

insert_photo_in_folder(new_dir, image_getted)