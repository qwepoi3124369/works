from sqlalchemy import create_engine
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as pl
engine = create_engine('postgresql://postgres:3124369@localhost:5432/gis')
sql = 'select * from house'
print(sql)
gdf = gpd.read_postgis(sql, engine, geom_col="geometry")  ##geom_col的預設值是geom要改
a = gdf.to_crs(epsg=4326)







b1=a['每坪月']
b2=sorted(b1)
N1=len(b2)


b3=len(b2)/4

Q1=b2[1163]

b4=b3*2
Q2=(b2[2325]+b2[2326])/2
b5=b3*3

Q3=b2[3488]

b6=sum(b1)/len(b1)

B1=[]
for i in b1:

    if i <= Q1:
        B1.append(1)
    elif Q1 < i <= Q2:
        B1.append(2)
    elif Q2 < i <= Q3:
        B1.append(3)
    else:
        B1.append(4)
print(B1)

C1=[]
c1=a['設備分n']
c2=sorted([i for i in c1 if i<100])
N2=len(c2)
c3=len(c2)/4
c4=c3*2
c5=c3*3

q1=c2[1157]
q2=c2[2314]
q3=c2[3471]
for i in c1:

    if i <= q1:
        C1.append(1)
    elif q1 < i <= q2:
        C1.append(2)
    elif q2 < i <= q3:
        C1.append(3)
    elif 100>i>q3:
        C1.append(4)
    else:
        C1.append(100)
print(C1)


d1=a['500bufferc']
d2=sorted(d1)
N3=len(d2)

d3=len(d2)/4

aQ1=d2[1163]

d4=d3*2
aQ2=(d2[2325]+d2[2326])/2


aQ3=d2[3488]

d6=sum(d1)/len(d1)

D1=[]
for i in d1:

    if i <= aQ1:
        D1.append(1)
    elif aQ1 < i <= aQ2:
        D1.append(2)
    elif aQ2 < i <= aQ3:
        D1.append(3)
    else:
        D1.append(4)
print(D1)

F1=[]
E1=[]
for i in range(len(B1)):
    if C1[i]!=100:
        a=round(0.35*B1[i]+0.3*C1[i]+0.35*D1[i],2)
        E1.append(a)
    else:
        E1.append(100)

e2=sorted([i for i in E1 if i<100])
N4=len(e2)
e3=len(e2)/4
e4=e3*2
e5=e3*3

bq1=e2[1157]
bq2=e2[2314]
bq3=e2[3471]
for i in E1:

    if i <= bq1:
        F1.append(1)
    elif bq1 < i <= bq2:
        F1.append(2)
    elif bq2 < i <= bq3:
        F1.append(3)
    elif 100>i>bq3:
        F1.append(4)
    else:
        F1.append(100)
print(F1)







print(N1,N2,N3)


print(E1)
import numpy as np
label1=['rent']
pl.boxplot(b2,labels=label1)
pl.show()


label2=['equipment']
pl.boxplot(c2,labels=label2)
pl.show()


label3=['convenient']
pl.boxplot(d2,labels=label3)
pl.show()