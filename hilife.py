import time
from selenium import webdriver
import geocoding3
import sqlite3
con = sqlite3.connect('house.db')
cur = con.cursor()
##cur.execute('''CREATE TABLE hilife('店名','區','地址','經度','緯度')''')
cur.execute('''DELETE FROM hilife''')##清空資料

options = webdriver.ChromeOptions()
options.add_argument("headless") ##背景執行


html='https://www.hilife.com.tw/storeInquiry_street.aspx'
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(html)
driver.find_element_by_xpath('//*[@id="CITY"]/option[14]').click()


name=[]
counties=[]
address=[]
long=[]
lat=[]
driver.find_element_by_id()
for i in range(1,27):
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="AREA"]/option[%d]'%i).click()
        d=driver.find_element_by_xpath('//*[@id="AREA"]/option[%d]'%i).text
        c=1
        while 2>1:

            try:
                a = driver.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div/div/table/tbody/tr[%d]/th[2]' % c).text
                b = driver.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div/div/table/tbody/tr[%d]/td[1]/a' % c).text
                c += 1
                f = str(b).split('號')[0]+'號'
                g = f.find('高')
                h = ''
                for i in range(g):
                    h += f[i]
                k = f.lstrip(h)
                print(k)

                if ',' in k:
                    k=k.split(',')[0]+'號'
                    name.append(a)
                    counties.append(d)
                    address.append(k)
                    print(k)
                elif '/' in k:
                    k = k.split('/')[0] + '號'
                    name.append(a)
                    counties.append(d)
                    address.append(k)
                elif '.' in k:
                    k = k.split('.')[0] + '號'
                    name.append(a)
                    counties.append(d)
                    address.append(k)

                else:
                    name.append(a)
                    counties.append(d)
                    address.append(k)
                    print(k)

            except:
                break
driver.close()





e=geocoding3.geocoding(address)
for i in range(len(e)):
    long.append(e[i][0])
    lat.append(e[i][1])



print(name,counties,address,long,lat)
for i in range(len(name)):
    cur.execute("INSERT INTO hilife VALUES ('%s','%s','%s',%f,%f)" % (name[i],counties[i],address[i], float(long[i]), float(lat[i])))
    con.commit()
con.close()
#地址到號
