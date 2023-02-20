import requests
from bs4 import BeautifulSoup

r = requests.get("https://tioj.ck.tp.edu.tw/users/chrislaiisme")
# print(r.text)

soup = BeautifulSoup(r.text,"html.parser")
sel = soup.select("div.col-md-8 a")

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

print("Success:")
for i in success:
    print(i)
