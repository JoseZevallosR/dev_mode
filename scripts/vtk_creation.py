import os
import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

try:
    import flopy
except:
    fpth = os.path.abspath(os.path.join("..", ".."))
    sys.path.append(fpth)
    import flopy

from flopy.export import vtk


workspace = '../examples/out/angascancha/vtk_files'
if not os.path.isdir(workspace):
    os.makedirs(workspace, exist_ok=True)

print(sys.version)
print("flopy version: {}".format(flopy.__version__))

np.set_printoptions(precision=4, suppress=True)

sys.path.insert(0, '../src/')

import warnings
warnings.filterwarnings('ignore')

model_name = 'regional_model'
model_path = '../examples/out/angascancha/model/'
exe_name = '../exe/mf6.exe'

#load the regional model
sim = flopy.mf6.MFSimulation.load(model_name+'.nam',sim_ws=model_path,exe_name=exe_name)
gwf = sim.get_model()

model_output_dir = os.path.join(workspace,'heads_vtk', "model_output_test")

# import the HeadFile reader and read in the head file
from flopy.utils import HeadFile

head_file = os.path.join(model_path, model_name+".hds")
hds = HeadFile(head_file)


# create the vtk object and export heads
vtkobj = vtk.Vtk(gwf, xml=True, pvd=False, vertical_exageration=2)
vtkobj.add_heads(hds)
vtkobj.write(os.path.join(workspace, "heads_output", "regional_model_head.vtu"))