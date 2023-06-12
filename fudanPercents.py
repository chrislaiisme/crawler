import requests as req
from bs4 import BeautifulSoup as bs

link = "https://www.fdhs.tyc.edu.tw/e-fdhs/news/out_news_detail_80.php?news_id="

"""
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

arr = [558, 541, 523, 499, 467, 437, 406, 377, 346, 321, 278, 251, 204, 169] # id
year= [111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100,  99,  98] # year
chart = [] # chart
schools = ["國立臺灣大學", "國立清華大學", "國立交通大學", "國立陽明交通大學", "國立成功大學", "國立政治大學"] # schools

for i in range(0, len(arr)):
    tmp = [year[i]] # the ith row in chart
    res = req.get(link+str(arr[i]))
    res.encoding = 'big5'
    soup = bs(res.text, "html.parser")
    s = soup.get_text();  
    count = 0 # number of people
    for j in range(0, len(schools)):
        start = 0
        end = len(s)
        s2 = schools[j]
        while True:
            p = s.find(s2, start, end)
            if p == -1:
                break
            count += 1
            start = p + 1
        if j == 0:
            tmp.append(count)
    tmp.append(count)
    chart.append(tmp)

s = "------|------|-------"
print("  Year|   NTU|   TFU")
print(s)
for i in chart:
    for j in range(0, 3):
        print('{:6}'.format(i[j]), end = ('\n' if j == 2 else '|'))
