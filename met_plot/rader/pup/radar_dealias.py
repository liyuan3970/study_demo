import matplotlib.pyplot as plt
import netCDF4
import pyart

RADAR_NAME = 'cfradial.nc'

# read in the data
radar = pyart.io.read_cfradial(RADAR_NAME)
print(radar.fields.keys())

# create a gate filter which specifies gates to exclude from dealiasing
gatefilter = pyart.filters.GateFilter(radar)
gatefilter.exclude_transition()
gatefilter.exclude_invalid('velocity')
gatefilter.exclude_invalid('reflectivity')
gatefilter.exclude_outside('reflectivity', 0, 80)

dealias_data = pyart.correct.dealias_fourdd(radar, gatefilter=gatefilter)
radar.add_field('corrected_velocity', dealias_data)