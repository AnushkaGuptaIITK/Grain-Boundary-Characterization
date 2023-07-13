import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np


# Data for plotting
file_name = "gb.csv"
data = np.genfromtxt(file_name, delimiter=',', dtype=str)

colors_arr = ["black", "red"]
markers_arr = ["o", "^"]

angles = data[1:, 0].astype(float)
gb_types = list(data[0, 1:])
gb_energies = data[1:, :].astype(float)

fig, ax = plt.subplots()

x = data[1:, 0].astype(float)
for gb in gb_types:
    ind = gb_types.index(gb)
    y = gb_energies[:, ind+1]

    ax.plot(x, y, linestyle="-", marker=f'{markers_arr[ind]}', markersize=6,
            color=f'{colors_arr[ind]}', label=gb)

# set labels and font size
ax.set_xlabel('tilt angle (degrees)', fontsize=16)
ax.set_ylabel('Grain boundary energy(J/m$^2$)', fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
ax.set_xlim(0, 180)
ax.set_ylim(0, 2.5)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig("gb.png", dpi=300)