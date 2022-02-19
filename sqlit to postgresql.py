import geopandas as gpd
import pandas as pd
import sqlite3
from shapely.geometry import Point
from sqlalchemy import create_engine
import matplotlib.pyplot as pl


engine = create_engine('postgresql://postgres:3124369@localhost:5432/gis')
con = sqlite3.connect('house.db')
cur = con.cursor()
df = pd.read_sql_query("SELECT * FROM house", con)
cur.close()
geom = [Point(xy) for xy in zip(df.經度, df.緯度)]
crs ={'init': 'epsg:4326'}
gdf = gpd.GeoDataFrame(df, crs=crs, geometry=geom)
gdf=gdf.to_crs(epsg=3826)
gdf.plot
pl.show()
print(gdf)

gdf.to_postgis('house',engine)###不要大小寫混合