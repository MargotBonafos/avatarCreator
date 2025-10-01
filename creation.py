from random import randint
import requests
from pathlib import Path

### 
# Open a file (dictionnary), get a ramdom number and choose the name of the line of the ramdom number
# parameters : file_name : the dictionnary in which the name is choosen 
# return the name choosen
### 
def choose_random_string(file_name):
    with open(file_name, "r", encoding="utf8") as f:
        lines = f.readlines()
        line_choice = randint(0, len(lines) - 1)
        name = lines[line_choice].strip()
    return name

### 
# Create a directory with all informations about the new avatar
# parameters : completeName : the name of the folder
# return the Path created
### 
def create_folder(completeName ):
    dir = Path(f"results/{completeName}")
    dir.mkdir(parents=True, exist_ok=True)
    return dir

### 
# Insert the ramdom photo of the avatar in the corresponding folder
# parameters : dir : the path of the folder, img : the photo in bytes
### 
def insert_photo_in_folder(dir, img):
    photo_name = f"{dir.name}_photo.png" 
    (dir / photo_name).write_bytes(img)

### 
# Get a ramdom avatar from the website https://thispersondoesnotexist.com/
# return : the image in bytes
### 
def thisPersonDoesNotExist_request():
    s = requests.Session()
    s.headers.update({"User-Agent":"YourTool/1.0"})
    r = s.get("https://thispersondoesnotexist.com/")
    r.raise_for_status()

    img = r.content

    return img


name = choose_random_string("names_dictionnary.txt")

surname = choose_random_string("surnames_dictionnary.txt")

img = thisPersonDoesNotExist_request()

dir = create_folder(f"{name}_{surname}")

insert_photo_in_folder(dir, img)