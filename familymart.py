import requests
from fake_useragent import UserAgent
import json
import sqlite3
con = sqlite3.connect('house.db')
cur = con.cursor()
##cur.execute('''CREATE TABLE familymart('店名','經度','緯度')''')
cur.execute('''DELETE FROM familymart''')##清空資料




counties=['鳳山區', '鹽埕區', '鼓山區', '林園區', '大寮區', '左營區', '大樹區', '楠梓區', '大社區', '三民區', '仁武區', '新興區', '前金區', '鳥松區', '岡山區', '苓雅區', '前鎮區', '橋頭區', '燕巢區', '旗津區', '田寮區', '小港區', '阿蓮區', '路竹區', '湖內區', '茄萣區', '永安區', '彌陀區', '梓官區', '旗山區', '美濃區', '六龜區', '甲仙區', '杉林區', '內門區', '桃源區']
for j in counties:
    print(j)
    html = 'https://api.map.com.tw/net/familyShop.aspx?searchType=ShopList&type=&city=高雄市&area=%s&road=&fun=showStoreList&key=6F30E8BF706D653965BDE302661D1241F8BE9EBC'%j
    useragent = UserAgent().random
    headers = {'user-agent': useragent, 'Referer': 'https://www.family.com.tw/'}
    a = requests.get(html, headers=headers)
    b = a.text
    c = str(b).split('(')[1].split(')')[0]
    d = json.loads(c)

    for i in range(len(d)):
        name = d[i]['NAME']
        long = d[i]['px']
        lat = d[i]['py']
        print(name, long, lat)
        cur.execute("INSERT INTO familymart VALUES ('%s',%f,%f)" % (name,float(long), float(lat)))
        con.commit()
con.close()





#<a href="#" onclick="showAdminArea('高雄市')">高雄市</a>
