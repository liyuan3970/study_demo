import cinrad
from cinrad.visualize import PPI
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
file = '/home/liyuan3970/Data/data/meto_data/radar_typhoon_liqima/wenzhou_rada/09/'
filename = r"Z_RADR_I_Z9577_20190809150400_O_DOR_SA_CAP.bin.bz2"
f3 = cinrad.io.CinradReader(file + filename)
# rl = list(f.iter_tilt(230, 'REF'))


v3 = f3.get_data(0, 230, 'REF')



rl = [f3.get_data(i, 230, 'REF') for i in f3.angleindex_r]
vcs = cinrad.easycalc.VCS(rl)
# 0度对应正北方向
sec = vcs.get_section(start_cart=(121.6, 28.2), end_cart=(120.1, 28.6))
fig = cinrad.visualize.PPI(v3, dpi=75)
plt.show()
#fig.plot_range_rings([50, 100, 150, 200, 230])
fig.plot_cross_section(sec)
plt.show()