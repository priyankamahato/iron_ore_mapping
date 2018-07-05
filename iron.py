import folium

import pandas

data = pandas.read_csv("Iron_Ore_1.csv")

lat=list(data["LATDD"])
lon=list(data["LONDD"])
state=list(data["STATE"])
locality=list(data["LOCALITY"])
met=list(data["METALLOGENESIS"])
top=list(data["TOPOSHEET"])
com=list(data["COMMODITY"])

def color_producer(lii):
    if lii =="JHARKHAND" :
        return "red"
    elif lii=="KARNATAKA":
        return "orange"
    elif lii=="CHATTISGARH":
        return "blue"
    elif lii=="ORISSA":
        return "green"
    elif lii=="MAHARASTRA":
        return "black"
    else:
        return "brown"

html = """<h4>Iron Ore Resource </h4>

      <strong>latitude:</strong>%s <br>
      <strong>longitude:</strong>%s <br>
<strong>state:</strong>%s <br>
<strong>locality:</strong>%s <br>
<strong>metallogenisis:</strong>%s <br>
<strong>topsheet:</strong>%s <br>
<strong>commodity:</strong>%s <br>
"""


map = folium.Map(location=[24.000000, 82.000000], zoom_start=5, tiles="OpenStreetMap")

#map.fit_bounds([[24.000000, 82.000000], [25.000000, 83.000000]])

tile2 = folium.TileLayer('Mapbox Bright')

map.add_child(tile2)

fgv = folium.FeatureGroup(name="Iron")

for lt, ln, li,lo,me,to,co in zip(lat, lon,state,locality,met,top,com):

    iframe = folium.IFrame(html=html %(str(lt),str(ln),str(li),str(lo),str(me),str(to),str(co)) , width=200,height=300)

    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=folium.Popup(iframe),

    fill_color=color_producer(li), fill=True,  color = 'grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

def style_function(x):

    return {'fillColor':'green' if x['properties']['POP2005'] <= 20000000 else 'orange' if 20000000 < x['properties']['POP2005'] < 50000000 else 'red'}

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),

style_function=style_function))

map.add_child(fgp)

map.add_child(fgv)

map.add_child(folium.LayerControl())

map.save("Mapi.html")
