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
bln2 = False # data without horizontal bars
bln3 = False # When data starts
chart = []
put = False # put arr in chart?
arr = [] # array -> chart
tmp = "" # string -> array

for ch in sel :
    if ch != "建" and bln3 == False: continue
    bln3 = True
    if ch == "資": break # "資" from "資料來源"
    
    if (ch == " " or ch == "\n") and (bln == True):
        arr.append(tmp)
        tmp = ""
    
    # bln
    if ch == " " or ch == "\n": bln = False
    else: bln = True
    if bln == False: continue
    
    #bln2
    if ch == "-": bln2 = False
    if ch == "建" or ch == "再" or ch == "惠": bln2 = True # "建" from "建國中學", "再" from "再興中學", "惠" from "惠文高中"
    if bln2 == False: continue
    
    #put
    if (u'\u4e00' <= ch <= u'\u9fff' and len(arr) > 1) or (len(arr) == 3): put = True
    
    if put == True:
        if len(arr) == 2:
            arr.insert(1, '?')
        chart.append(arr)
        # print(chart)
        arr = []
        put = False
    
    tmp = tmp + ch
    
    # print(chart)
    
s = "-------------|----------|----------"
print("  School     |   NTU    |  TFU  ")
print(s)
for i in chart: 
    if(i[0] == "再興中學"):
        print("-----------------------------------")
        print("此線以上為明星高中(NTU 7%, TFU 30%)")
        print("-----------------------------------")
    if(i[0] == "惠文高中"):
        print("-----------------------------------")
        print("此線以上為前段高中(TFU 8.6%)")
        print("-----------------------------------")
    if(i[0] == "復旦高中"):
        print("===================================")
    for j in range(0, 3):
        print('  {:8}'.format(i[j]), end = (' <-- 復旦在這裡\n' if (i[0] == "復旦高中" and j == 2) else ('\n' if j == 2 else '|')))
    if(i[0] == "復旦高中"):
        print("===================================")
