import requests as req
from bs4 import BeautifulSoup as bs

link = "https://www.ptt.cc/bbs/SENIORHIGH/M.1661937809.A.4EE.html"; # [情報] 111年高中升學率 - 看板 SENIORHIGH - 批踢踢實業坊
res = req.get(link)
soup = bs(res.text, "html.parser")
psr = {
    "id" : "main-content",
    "class" : "bbs-screen bbs-content"
}
sel = str(soup.find("div", psr))
# print(sel)

bln = False # the data that should be in the chart
bln2 = False # data without space
bln3 = False # data without minus
cnt = 0 # counting elements put in the chart
chart = [["School", "NTU", "TTYCC"]]
arr = [] # array -> chart
tmp = "" # string -> array

for ch in sel :
    if ch == "建" : bln = True # "建" from "建國中學"
    if ch == "資" : break # "資" from "資料來源"
    if ch == " " or ch == "\n" : bln2 = False
    else : bln2 = True
    if ch == "-" : bln3 = False
    if ch == "再" or ch == "惠" : bln3 = True # "再" from "再興中學", "惠" from "惠文高中"
    
    if not bln2 and tmp != "" : 
        arr.append(tmp)
        tmp = ""
        cnt += 1
    if cnt == 3 :
        chart.append(arr)
        arr = []
        cnt = 0 
    
    if not bln or not bln2 or not bln3 : continue
    tmp += ch
    
print(chart)
