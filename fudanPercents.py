import requests as req

from bs4 import BeautifulSoup as bs

link = "https://www.fdhs.tyc.edu.tw/e-fdhs/news/out_news_detail_80.php?news_id="
for i in range(572, 0, -1):
    res = req.get(link+str(i))
    res.encoding = 'big5'
    soup = bs(res.text, "html.parser")
    goal = soup.find(string="簡單") # find "簡單"
    goal = goal.parent.parent.parent.parent # go back to parent
    goal = goal.find_all("td")[1].find("font") # find real goal text
    if goal.text.find("放榜") != -1:
        print(str(i) + ":\n" + goal.text + "\n==================================================\n")
print("Finish")

arr = [558, 541, 523, 495, 000, 428, 000, 370, ]
