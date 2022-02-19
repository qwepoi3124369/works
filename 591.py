from selenium import webdriver
import time
import sqlite3
import requests
import json



def houseurl():
    con = sqlite3.connect('house.db')
    cur = con.cursor()
    ##cur.execute('''CREATE TABLE house('地址','坪數','租金','緯度','經度','冰箱', '洗衣機', '電視', '冷氣', '熱水器', '床', '衣櫃', '第四台', '網路', '天然瓦斯', '沙發', '桌椅', '陽台', '電梯', '車位')''')
    ##cur.execute('''DELETE FROM house''')##清空資料



    driver = webdriver.Chrome()
    url1 = 'https://rent.591.com.tw/?kind=0&region=17&shType=list'
    driver.get(url1)
    driver.maximize_window()

    time.sleep(10)

    page = driver.find_element_by_xpath('//*[@id="rent-list-app"]/div/div[3]/div/section[4]/div/a[7]').text##頁數
    print(page)
    page1 = int(page)
    time.sleep(3)




    headers = {'Accept': '*/*',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
               'Connection': 'keep-alive',
               'device': 'pc',
               'deviceid': '0fdsprfmljo8343edq8uud49b1',
               'Host': 'bff.591.com.tw',
               'Origin': 'https://rent.591.com.tw',
               'Referer': 'https://rent.591.com.tw/',
               'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
               'sec-ch-ua-mobile': '?0',
               'sec-ch-ua-platform': "Windows",
               'Sec-Fetch-Dest': 'empty',
               'Sec-Fetch-Mode': 'cors',
               'Sec-Fetch-Site': 'same-site',
               'token': 'l53hd035rt03p1auccljhkbf85',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
               'X-CSRF-TOKEN': 'DItyKAZtllSmHtNTqRAApKMwNfKhWS7JYcVP3LN9'}

    for i in range(1, 31):

        try:
            a = driver.find_element_by_xpath('// *[ @ id = "rent-list-app"] / div / div[3] / div / section[3] / div / section[%d] / a / div[2] / div[2]' % i).text  # 地址
        except:
            time.sleep(10)
            a = driver.find_element_by_xpath('// *[ @ id = "rent-list-app"] / div / div[3] / div / section[3] / div / section[%d] / a / div[2] / div[2]' % i).text  # 地址





        b = driver.find_element_by_xpath('//*[@id="rent-list-app"]/div/div[3]/div/section[3]/div/section[%d]/a/div[2]/ul[2]/li[2]' % i).text  # 坪數
        b2 = driver.find_element_by_xpath('// *[ @ id = "rent-list-app"] / div / div[3] / div / section[3] / div / section[%d] / a / div[2] / ul[2] / li[3]' % i).text  # 坪數
        b3=(b+','+b2)
        b4=str(b3).split(',')
        if str(b4[0])[-1]=='坪':
            b5=b4[0]
        else:
            b5=b4[1]

        c = driver.find_element_by_xpath('//*[@id="rent-list-app"]/div/div[3]/div/section[3]/div/section[%d]/a/div[2]/div[5]' % i).text#租金
        d = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/section[3]/div/section[%d]/a' % i).get_attribute("href")##網址

        e=str(d).split('-')[-1].split('.')[0]
        f='https://bff.591.com.tw/v1/house/rent/detail?id=%s'%e
        html = requests.get(f, headers=headers)
        g = json.loads(html.text)
        h = g['data']["positionRound"]['lat']
        k = g['data']["positionRound"]['lng']
        l = g['data']['service']['facility']
        a1 = []

        for i1 in range(len(l)):
            m = g['data']['service']['facility'][i1]['name']
            n = g['data']['service']['facility'][i1]['active']
            print(m, n)
            if n == 1:
                a1.append(n)
            else:
                a1.append(n)

        print(a1)
        a2 = tuple(a1)
        print(a2)
        print(d, b5, c,f,h,k)
        try:
            cur.execute("INSERT INTO house VALUES ('%s','%s','%s',%f,%f,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"%(a,b5,c,float(h),float(k)),a2)
        except:
            a3=('null','null','null','null','null','null','null','null','null','null','null','null','null','null','null')
            cur.execute("INSERT INTO house VALUES ('%s','%s','%s',%f,%f,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)" % (a, b5, c, float(h), float(k)), a3)

        con.commit()

    for j in range(int(page1 - 1)):

        try:
            driver.find_element_by_class_name("pageNext").click()
            time.sleep(1)
        except:
            time.sleep(5)
            driver.find_element_by_class_name("pageNext").click()
            time.sleep(1)

        for i in range(1, 31):
            try:

                a = driver.find_element_by_xpath(
                    '// *[ @ id = "rent-list-app"] / div / div[3] / div / section[3] / div / section[%d] / a / div[2] / div[2]' % i).text  # 地址
                b = driver.find_element_by_xpath(
                    '//*[@id="rent-list-app"]/div/div[3]/div/section[3]/div/section[%d]/a/div[2]/ul[2]/li[2]' % i).text  # 坪數
                b2 = driver.find_element_by_xpath(
                    '// *[ @ id = "rent-list-app"] / div / div[3] / div / section[3] / div / section[%d] / a / div[2] / ul[2] / li[3]' % i).text
                b3 = (b + ',' + b2)
                b4 = str(b3).split(',')
                if str(b4[0])[-1] == '坪':
                    b5 = b4[0]
                else:
                    b5 = b4[1]


                c = driver.find_element_by_xpath(
                    '//*[@id="rent-list-app"]/div/div[3]/div/section[3]/div/section[%d]/a/div[2]/div[5]' % i).text  # 租金
                d = driver.find_element_by_xpath(
                    '/html/body/div[2]/div/div[3]/div/section[3]/div/section[%d]/a' % i).get_attribute("href")  ##網址
                e = str(d).split('-')[-1].split('.')[0]
                f = 'https://bff.591.com.tw/v1/house/rent/detail?id=%s' % e
                html = requests.get(f, headers=headers)
                g = json.loads(html.text)
                h = g['data']["positionRound"]['lat']
                k = g['data']["positionRound"]['lng']
                l = g['data']['service']['facility']
                a1 = []

                for i1 in range(len(l)):
                    m = g['data']['service']['facility'][i1]['name']
                    n = g['data']['service']['facility'][i1]['active']
                    print(m, n)
                    if n == 1:
                        a1.append(n)
                    else:
                        a1.append(n)

                print(a1)
                a2 = tuple(a1)
                print(a2)
                print(d, b5, c, f, h, k)

                try:
                    cur.execute("INSERT INTO house VALUES ('%s','%s','%s',%f,%f,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)" % (
                    a, b5, c, float(h), float(k)), a2)
                except:
                    a3 = (
                    'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null',
                    'null', 'null', 'null')
                    cur.execute("INSERT INTO house VALUES ('%s','%s','%s',%f,%f,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)" % (
                    a, b5, c, float(h), float(k)), a3)
                con.commit()

            except:
                try:
                    time.sleep(1)
                    a = driver.find_element_by_xpath(
                        '// *[ @ id = "rent-list-app"] / div / div[3] / div / section[3] / div / section[%d] / a / div[2] / div[2]' % i).text  # 地址
                    b = driver.find_element_by_xpath(
                        '//*[@id="rent-list-app"]/div/div[3]/div/section[3]/div/section[%d]/a/div[2]/ul[2]/li[2]' % i).text  # 坪數
                    b2 = driver.find_element_by_xpath(
                        '// *[ @ id = "rent-list-app"] / div / div[3] / div / section[3] / div / section[%d] / a / div[2] / ul[2] / li[3]' % i).text
                    c = driver.find_element_by_xpath(
                        '//*[@id="rent-list-app"]/div/div[3]/div/section[3]/div/section[%d]/a/div[2]/div[5]' % i).text  # 租金
                    d = driver.find_element_by_xpath(
                        '/html/body/div[2]/div/div[3]/div/section[3]/div/section[%d]/a' % i).get_attribute("href")  ##網址
                    b3 = (b + ',' + b2)
                    b4 = str(b3).split(',')
                    if str(b4[0])[-1] == '坪':
                        b5 = b4[0]
                    else:
                        b5 = b4[1]

                    e = str(d).split('-')[-1].split('.')[0]
                    f = 'https://bff.591.com.tw/v1/house/rent/detail?id=%s' % e
                    html = requests.get(f, headers=headers)
                    g = json.loads(html.text)
                    h = g['data']["positionRound"]['lat']
                    k = g['data']["positionRound"]['lng']
                    l = g['data']['service']['facility']
                    a1 = []

                    for i1 in range(len(l)):
                        m = g['data']['service']['facility'][i1]['name']
                        n = g['data']['service']['facility'][i1]['active']
                        print(m, n)
                        if n == 1:
                            a1.append(n)
                        else:
                            a1.append(n)

                    print(a1)
                    a2 = tuple(a1)
                    print(a2)
                    print(d, b5, c, f, h, k)

                    try:
                        cur.execute("INSERT INTO house VALUES ('%s','%s','%s',%f,%f,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)" % (
                        a, b5, c, float(h), float(k)), a2)
                    except:
                        a3 = (
                        'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null',
                        'null', 'null', 'null')
                        cur.execute("INSERT INTO house VALUES ('%s','%s','%s',%f,%f,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)" % (
                        a, b5, c, float(h), float(k)), a3)
                    con.commit()
                except:
                    print(1)
    con.close()
    driver.close()
houseurl()


