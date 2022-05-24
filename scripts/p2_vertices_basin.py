import sys
sys.path.insert(0, 'd:/Proyectos_GitHub/dev_mode/src')
from meshProperties import mesh_shape


mesh=mesh_shape('../examples/out/angascancha/voronoiRegions.shp')
gridprops=mesh.get_gridprops_disv()
mesh.save_properties('../examples/out/angascancha/json/disvDict.json')
