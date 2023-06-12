import requests as req
from bs4 import BeautifulSoup as bs

"""
link = "https://www.fdhs.tyc.edu.tw/e-fdhs/news/out_news_detail_80.php?news_id="
for i in range(573, 0, -1):
    res = req.get(link+str(i))
    res.encoding = 'big5'
    soup = bs(res.text, "html.parser")
    goal = soup.find(string="簡單") # find "簡單"
    goal = goal.parent.parent.parent.parent # go back to parent
    goal = goal.find_all("td")[1].find("font") # find real goal text
    if goal.text.find("大學") != -1:
        print(str(i) + ":\n" + goal.text + "\n==================================================\n")
print("Finish")
"""

arr = [558, 541, 523, 499, 467, 437, 406, 377, 346, 321, 278, 251, 204, 169]
year= [111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100,  99,  98]
