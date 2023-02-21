import requests
from bs4 import BeautifulSoup

while True:
    Id = input("Please input your TIOJ id: \n")
    
    r = requests.get("https://tioj.ck.tp.edu.tw/users/" + Id)
    # print(r.text)
    
    soup = BeautifulSoup(r.text,"html.parser")
    sel = soup.select("div.col-md-8 a")
    
    if len(sel) == 0:
        print("Id doesn't exist")
        continue
    
    success = []
    muted = []
    warning = []

    for i in sel:
        s = i["class"][0]
        s2 = i.text

        if s == "text-success":
            success.append(s2)
        elif s == "text-warning":
            warning.append(s2)
        else:
            muted.append(s2)

    print("AC:")
    for i in success:
        print(i)

    '''
    print()
    print("WA:")
    for i in warning:
        print(i)
    print()
    print("None:")
    for i in muted:
        print(i)
    '''
