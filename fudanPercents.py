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

arr = [574, 558, 541, 523, 499, 467, 437, 406, 377, 346, 321, 278, 251, 204, 169] # id
year= [112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100,  99,  98] # year
nop = [558,   0, 562,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0]
chart = [] # chart
schools = ["國立臺灣大學", "國立清華大學", "國立交通大學", "國立陽明交通大學", "國立成功大學", "國立政治大學"] # schools
dft_nop = 565 # default nop

for i in range(0, len(arr)):
    tmp = [year[i]] # year
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
            tmp.append(count) # NTU
    tmp.append(count) # TFU
    tmp.append('?' if nop[i] == 0 else nop[i]) # NOP
    num = dft_nop if tmp[3] == '?' else tmp[3]
    tmp.append(str(round(tmp[1]/num*100, 2)) + '%') # NTU%
    tmp.append(str(round(tmp[2]/num*100, 2)) + '%') # TFU%
    chart.append(tmp) # append row in chart

s = ''
for i in range(0, 6):
    s += '-------'
    if i != 5:
        s += '|'
print("   Year|    NTU|    TFU|    NOP|   NTU%|   TFU%")
print(s)
for i in chart:
    for j in range(0, 6):
        print('{:>7}'.format(i[j]), end = ('\n' if j == 5 else '|'))
print('Average:')
NTUn = 0
TFUn = 0
NOPn = 0
for i in chart:
    NTUn += i[1]
    TFUn += i[2]
    NOPn += dft_nop if i[3] == '?' else i[3]
print()
print("NTU%: ", end = '')
print(str(round(NTUn/NOPn*100, 2)) + '%')
print("TFU%: ", end = '')
print(str(round(TFUn/NOPn*100, 2)) + '%')
print()
print("* NTU = National Taiwan University")
print("* TFU = Top Five Universities")
print("* NOP = Number Of People (565 by default if there's no data)")
print()
print("* The number 565 comes from \"https://www.fdhs.tyc.edu.tw/campus/brief.htm\" with 3391/6 = 565.166666667")
print("* All data are from \"https://www.fdhs.tyc.edu.tw/\"")
