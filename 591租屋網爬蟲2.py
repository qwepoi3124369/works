import requests
import pandas as pd
from bs4 import BeautifulSoup



a=pd.read_excel('C:/Users/qwepo/Desktop/web9.xlsx',header=None)
f=len(a[0])
h=[]
n=[]
j=[]

for i in range(f):
    print(i)
    g=a[1][i+1]
    print(g)
    url="%s"%g
    html = requests.get(url)
    b=BeautifulSoup(html.text,'html.parser')
    data=b.find_all("div",{"class":"price clearfix"})
    print(data[0].text)
    k=data[0].text
    h.append(k)
    data2=b.find_all("ul",{"class":"attr"})
    print(data2[0].text)
    l=data2[0].text
    n.append(l)


o=pd.DataFrame(h,n)
o.to_excel('C:/Users/qwepo/Desktop/web9over.xlsx',encoding="utf-8-sig")


