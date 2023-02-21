import requests
from bs4 import BeautifulSoup
import random
import webbrowser

while True: 
    Id = input("Please input your TIOJ id: \n")

    r = requests.get("https://tioj.ck.tp.edu.tw/users/" + Id)
    # print(r.text)

    soup = BeautifulSoup(r.text,"html.parser")
    sel = soup.select("div.col-md-8 a")

    if len(sel) == 0:
        print("Id doesn't exist")
    else:
        break;

while True:
    op = int(input("Get a random problem from problems that you've:\n\t1. AC ed, 2. WA ed, 3. None touched")) - 1
    problems = []
    for i in range(0, 3):
        problems.append([])

    for i in sel:
        s = i["class"][0]
        s2 = i.text

        if s == "text-success":
            problems[0].append(s2)
        elif s == "text-warning":
            problems[1].append(s2)
        else:
            problems[2].append(s2)
            
    pos = int(random.randint(0, len(problems[op]) - 1))
    webbrowser.open_new_tab("https://tioj.ck.tp.edu.tw/problems/" + problems[op][pos])
