from selenium import webdriver
import time
import pandas as pd
driver=webdriver.Chrome()
url='https://rent.591.com.tw/?kind=0&region=17&school=3046&shType=list'
driver.get(url)
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="area-box-body"]/dl[3]/dd[1]').click()
time.sleep(10)
b=driver.find_element_by_xpath('//*[@id="container"]/section[5]/div/div[1]/div[5]/div/a[7]').text
print(b)
c=int(b)
d=[]
time.sleep(3)


driver.find_element_by_xpath('//*[@id="container"]/section[5]/div/div[1]/div[5]/div/a[1]/span').click()
time.sleep(3)
for i in range(1,c+1):

    a = driver.find_element_by_xpath('//*[@id="content"]/ul[%d]/li[2]/h3/a' % i).get_attribute("href")
    print(a)
    d.append(a)






for j in range(int(c-1)):
    try:
        driver.find_element_by_class_name("pageNext").click()
        time.sleep(1)
    except:
        time.sleep(5)
        driver.find_element_by_class_name("pageNext").click()
        time.sleep(1)




    for i in range(1,c+1):
        try:
            a=driver.find_element_by_xpath('//*[@id="content"]/ul[%d]/li[2]/h3/a'%i).get_attribute("href")
            print(a)
            d.append(a)

        except:
            try:
                time.sleep(5)
                a = driver.find_element_by_xpath('//*[@id="content"]/ul[%d]/li[2]/h3/a' % i).get_attribute("href")
                print(a)
                d.append(a)
            except:
                print(1)



e=pd.DataFrame(d)
e.to_excel('C:/Users/qwepo/Desktop/web9.xlsx',encoding="utf-8-sig")






