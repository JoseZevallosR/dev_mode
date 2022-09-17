import geopandas as gpd

mesh=gpd.read_file('D:/Proyectos_GitHub/gui_project/examples/in/shp/Angascancha_Basin_Extension.shp')

mapa=folium.Map(location=[maestro.LATITUD.mean(),maestro.LONGITUD.mean()],zoom_start=6)

print(mesh.centroid)