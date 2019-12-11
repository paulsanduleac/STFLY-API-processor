import requests
from itertools import product
from string import ascii_lowercase, digits
from datetime import datetime
import atexit, random

original_url = "" #original URL goes here
size=2
url_length=len(original_url)
url_new_length=url_length-size
url = ""

file=open("scrape"+str(datetime.now())+".txt","w")
api_url="" #API URL without UUID goes here
for i in range(0, url_new_length):
    url+=original_url[i]
url_list = []
combinations = list(product(ascii_lowercase + digits, repeat=32))
random.shuffle(combinations)
for i in range(1,1000):
    word = ""
    for letter in random.choice(combinations):
        word+=str(letter)
    uuid=word[0:8]+"-"+word[8:12]+"-"+word[12:16]+"-"+word[16:20]+"-"+word[20:32]
    response = requests.get(api_url+uuid)
    print(uuid)
    print(str(response.status_code))
    if response.status_code == "204":
        file.write(api_url+uuid+";"+str(response.status_code)+";none;\n")
    if response.status_code == "200":
        file.write(api_url+uuid+";"+str(response.status_code)+";"+str(response.text)+";\n")
atexit.register(file.close())