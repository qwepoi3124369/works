from selenium import webdriver
import time
import sqlite3
import geocoding3
con = sqlite3.connect('house.db')
cur = con.cursor()
##cur.execute('''CREATE TABLE SevenELEVEN('店名','區','地址','經度','緯度')''')
##cur.execute('''DELETE FROM SevenELEVEN''')##清空資料
options = webdriver.ChromeOptions()
options.add_argument("headless") ##背景執行


html='https://emap.pcsc.com.tw/emap.aspx'
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(html)
driver.find_element_by_xpath('//*[@id="maplink_kaohsiung"]').click()
counties=['鳳山區', '鹽埕區', '鼓山區', '林園區', '大寮區', '左營區', '大樹區', '楠梓區', '大社區', '三民區', '仁武區', '新興區', '前金區', '鳥松區', '岡山區', '苓雅區', '前鎮區', '橋頭區', '燕巢區', '旗津區', '田寮區', '小港區', '阿蓮區', '路竹區', '湖內區', '茄萣區', '永安區', '彌陀區', '梓官區', '旗山區', '美濃區', '六龜區', '甲仙區', '杉林區', '內門區', '桃源區']
name=[]
counties2=[]
address=[]
long=[]
lat=[]




for i in counties:
    time.sleep(1)
    a=driver.find_element_by_xpath('//*[@id="counties_s"]').text
    b='//*[ @ id = "town_%s"]'%i
    driver.find_element_by_xpath(b).click()


    time.sleep(5)
    try:
        while 1>0:
            try:
                e = 2
                while 1 > 0:


                    h = driver.find_element_by_xpath('// *[ @ id = "mytb"] / tbody / tr[%d] / td[2] / table / tbody / tr[1] / td[1]' % e).text
                    k=str(h).split('\n')[1].split('：')[1]
                    f = driver.find_element_by_xpath('//*[@id="mytb"]/tbody/tr[%d]/td[2]/table/tbody/tr[2]/td'%e).text
                    g=str(f).split('\n')[0].split('：')[1]
                    e=e+1
                    l=str(g).split('號')[0] + '號'
                    print(e)
                    if ',' in l:
                        l = l.split(',')[0] + '號'
                        name.append(k)
                        address.append(l)
                        counties2.append(i)
                        print(l)
                    elif '/' in l:
                        l = l.split('/')[0] + '號'
                        name.append(k)
                        address.append(l)
                        counties2.append(i)
                        print(l)
                    elif '.' in l:
                        l = l.split('.')[0] + '號'
                        name.append(k)
                        address.append(l)
                        counties2.append(i)
                        print(l)

                    else:
                        name.append(k)
                        address.append(l)
                        counties2.append(i)
                        print(l)

            except:
                driver.find_element_by_xpath(' // *[ @ id = "Next"]').click()
    except:
        driver.find_element_by_xpath('//*[@id="map_all_link1"]').click()



driver.close()

e=geocoding3.geocoding(address)
for i in range(len(e)):
    long.append(e[i][0])
    lat.append(e[i][1])
print(name,address,long,lat)


for i in range(len(name)):
    cur.execute("INSERT INTO SevenELEVEN VALUES ('%s','%s','%s',%f,%f)" % (name[i],counties2[i],address[i], float(long[i]), float(lat[i])))
    con.commit()
con.close()


