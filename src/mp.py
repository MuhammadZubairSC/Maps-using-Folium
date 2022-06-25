import folium, pandas
b=pandas.read_csv("Volcanoes_USA.txt")
coord=pandas.DataFrame([b["LAT"],b["LON"]])
coord=coord.T

mp=folium.Map(location=[38, -99], zoom_start=6, tiles="cartodb positron")

fg = folium.FeatureGroup(name="ZubairKing")

for i in coord.iloc:
    fg.add_child(folium.Marker(location=[i[0],i[1]], popup="Info", icon=folium.Icon(color="blue")))

mp.add_child(fg)
mp.save("mk.html")