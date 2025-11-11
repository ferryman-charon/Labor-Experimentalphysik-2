import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')
plt.rcParams.update({'font.size': 14})

delta_angle = 0.1
lila_full = np.array([285.9, 286.0, 286.0, 285.9, 284.1])
blue_angle = np.array([288.0, 283.3, 288.5])
dgrün_angel = np.array([290.5, 290.8, 291.1]) 
hgrün_angel = np.array([291.9, 292.3, 292.8]) 
yellow_full = np.array([292.6, 292.9, 293.5, 292.8, 293.5]) 
lila2 = np.array([286.2])
rot1 = np.array([294.2])
rot2 = np.array([295.0])

colors_list = [lila2, lila_full, blue_angle, dgrün_angel, hgrün_angel, yellow_full, rot1, rot2]
colors_plot = []

plt.tight_layout()
plt.show()