import xarray as xr
import numpy as np
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

# load nmc_met_io for retrieving micaps server data
from nmc_met_io.retrieve_micaps_server import get_model_grid, get_model_grids

directory = '/home/liyuan3970/study_demo/met_plot/miscaps/'
filename = '20062720.033'
data = get_model_grid(directory, filename=filename, cache=False)