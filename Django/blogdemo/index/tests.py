import numpy as np

import matplotlib.pyplot as mp
from matplotlib.figure import Figure      
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
fig=Figure(figsize=(6,6))
ax=fig.add_subplot(111)
x= np.linspace(-np.pi, np.pi, 1000)
y=np.sin(x)
ax.plot_date(x, y, '-')

