

import folium
from sqlalchemy import create_engine
import geopandas as gpd
import matplotlib.pyplot as pl

import pandas as pd


def map(counties):
    ##建立地圖
    m = folium.Map((22.9, 120.31), zoom_start=10)

    ##建立群集1
    from folium.plugins import MarkerCluster
    marker_cluster = MarkerCluster(name='house').add_to(m)  # 建立一個MakerCluster的物件讓物件指定到map

    ##資料庫
    engine = create_engine('postgresql://postgres:3124369@localhost:5432/gis')

    ##選取建立租屋
    sql = 'select * from house'
    print(engine)
    gdf = gpd.read_postgis(sql, engine, geom_col="geometry")  ##geom_col的預設值是geom要改
    a = gdf.to_crs(epsg=4326)
    print(a)
    ##b=a[a['電梯']=='1']

    for i in counties:
        b = a[(a['TOWNNAME'] == i)]
        print(type(b))
        b.reset_index(inplace=True)
        ##index重置成原本的樣子
        lat = b['geometry'].y
        long = b['geometry'].x
        print(lat)
        print(len(lat))
        print(len(long))
        print(len(b['電梯']))
        print(len(b['坪數']))

        for i in range(len(lat)):
            if str(b['租金等'][i])=='1':
                a1='極劣'
            elif str(b['租金等'][i])=='2':
                a1='劣'
            elif str(b['租金等'][i]) == '3':
                a1='好'
            elif str(b['租金等'][i]) == '4':
                a1='極好'

            if str(b['設備等'][i])=='1':
                b1='極劣'
            elif str(b['設備等'][i])=='2':
                b1='劣'
            elif str(b['設備等'][i]) == '3':
                b1='好'
            elif str(b['設備等'][i]) == '4':
                b1='極好'
            elif str(b['設備等'][i]) == '100':
                b1='無資料'

            if str(b['便利等'][i])=='1':
                c1='極劣'
            elif str(b['便利等'][i])=='2':
                c1='劣'
            elif str(b['便利等'][i]) == '3':
                c1='好'
            elif str(b['便利等'][i]) == '4':
                c1='極好'

            if str(b['總分等'][i])=='1':
                d1='極劣'
            elif str(b['總分等'][i])=='2':
                d1='劣'
            elif str(b['總分等'][i]) == '3':
                d1='好'
            elif str(b['總分等'][i]) == '4':
                d1='極好'
            elif str(b['總分等'][i]) == '100':
                d1='無資料'




            icon = folium.Icon(color="red", icon_color="blue", icon='fa-home', prefix='fa')
            folium.Marker(location=[lat[i], long[i]],
                          popup='##########################%s##########################%s##########################%s##########################%s##########################%s##########################%s##########################%s##########################%s' % (
                              '地址:' + str(b['地址'][i]), '坪數:' + str(b['坪數'][i]), '租金:' + str(b['租金'][i]),
                              '五百公尺內便利商店數:' + str(b['500bufferc'][i]) + '間','租金等級:'+str(b['租金等'][i])+a1,'設備等級:'+str(b['設備等'][i])+b1,'便利等級:'+str(b['便利等'][i])+c1,'總分等級:'+str(b['總分等'][i])+d1), icon=icon).add_to(marker_cluster)



    for i in counties:
        Kaohsiung = gpd.read_file('map/%s.shp' % str(i), encoding='utf-8')
        Kaohsiung.crs = {'init': 'epsg:3826'}
        Kaohsiung.to_crs(epsg=4326)

        print(Kaohsiung['TOWNNAME'])
        folium.GeoJson(Kaohsiung.to_json(), name=str(i)).add_to(m)


    from folium.plugins import MiniMap  ##迷你地圖
    folium.Marker()
    minimap = MiniMap()
    m.add_child(child=minimap)

    minimap = MiniMap(zoom_level_offset=-8)  ##縮放比例

    from folium.plugins import MeasureControl
    m.add_child(MeasureControl())  # 量測地圖功能加入

    folium.LayerControl().add_to(m)  ##加入圖層
    m.save('map.html')


    ##熱區地圖
    from folium.plugins import HeatMap # 導入套件
    Heatmap = folium.Map(location=[22.9, 120.31], zoom_start=10, tites='OpenStreetMap') # 產生一個新的地圖
    Heatdata = []
    lat2 = a['geometry'].y
    long2 = a['geometry'].x


    for i in range(len(lat2)):
        data = [lat2[i],long2[i]] # 這是準備要給HeatMap的資料，[[lat1,long1],[lat2,long2]...]
        Heatdata.append(data)
    Kaohsiung2 = gpd.read_file('map/Kaohsiung.shp', encoding='utf-8')
    Kaohsiung2.crs = {'init': 'epsg:3826'}
    Kaohsiung2.to_crs(epsg=4326)

    folium.GeoJson(Kaohsiung2.to_json(),name='Kaohsiung2').add_to(Heatmap)##高雄底圖
    HeatMap(Heatdata).add_to(Heatmap) #將資料放入HeatMap中，再指定到目標地圖上。
    Heatmap.save('Heatmap.html')

