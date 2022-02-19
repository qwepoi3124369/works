from selenium import webdriver
import geocoding3
import sqlite3
con = sqlite3.connect('house.db')
cur = con.cursor()
##cur.execute('''CREATE TABLE okmark('店名','地址','經度','緯度')''')
cur.execute('''DELETE FROM okmark''')##清空資料


options = webdriver.ChromeOptions()
options.add_argument("headless") ##背景執行

name=[]
address=[]
long=[]
lat=[]


html='https://www.okmart.com.tw/convenient_shopSearch#'
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(html)
driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ddlcity"]/option[16]').click()
c=1
try:
    while 2>1:
        a=driver.find_element_by_xpath('//*[@id="shopList"]/ul/li[%d]/h2'%c).text
        b=driver.find_element_by_xpath('//*[@id="shopList"]/ul/li[%d]/span'%c).text
        c+=1
        print(c,a,b)
        d=str(b).split('號')[0]+'號'
        if '/' in d:
            d=d.split('/')[0]+'號'
            name.append(a)
            address.append(d)
        elif '.' in d:
            d = d.split('.')[0] + '號'
            name.append(a)
            address.append(d)
        else:
            name.append(a)
            address.append(d)

except:
    driver.close()

e=geocoding3.geocoding(address)
for i in range(len(e)):
    long.append(e[i][0])
    lat.append(e[i][1])
print(name,address,long,lat)


for i in range(len(name)):
    cur.execute("INSERT INTO okmark VALUES ('%s','%s',%f,%f)" % (name[i],address[i], float(long[i]), float(lat[i])))
    con.commit()
con.close()







