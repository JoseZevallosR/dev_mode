import warnings
warnings.filterwarnings('ignore')

from scipy.interpolate import griddata
#from osgeo import osr
#from osgeo import gdal
#from osgeo import gdal_array
import rasterio
from rasterio.transform import from_origin
import geopandas as gpd

from shapely.geometry import mapping
from shapely.geometry import Polygon, Point, MultiLineString
from collections import OrderedDict
import pandas as pd
import numpy as np

#plots
import matplotlib.pyplot as plt

#modflow
import flopy
import flopy.discretization as fgrid
import flopy.plot as fplot
from flopy.utils.gridintersect import GridIntersect
import flopy.utils.binaryfile as bf

import os, json

import sys
sys.path.insert(0, '../src')
from meshProperties import mesh_shape

f=open('../examples/out/angascancha/json/disvDict.json')
gridprops = json.load(f)

cell2d = gridprops['cell2d']
vertices = gridprops['vertices']
ncpl = gridprops['ncpl']
nvert = gridprops['nvert']
centroids=[(x[0],x[1]) for x in gridprops['centroids']]

#Extact dem values for each centroid of the voronois
src = rasterio.open('../examples/in/rst/DEM_200b.tif')
elevation=[x for x in src.sample(centroids)]

nlay = 5

mtop=np.array([elev[0] for i,elev in enumerate(elevation)])
zbot=np.zeros((nlay,ncpl))


AcuifInf_Bottom = 3000
zbot[0,] = mtop - 30
zbot[1,] = AcuifInf_Bottom + (0.85 * (mtop - AcuifInf_Bottom))
zbot[2,] = AcuifInf_Bottom + (0.70 * (mtop - AcuifInf_Bottom))
zbot[3,] = AcuifInf_Bottom + (0.50 * (mtop - AcuifInf_Bottom))
zbot[4,] = AcuifInf_Bottom

print(mtop)
print(zbot)
print(mtop - AcuifInf_Bottom)