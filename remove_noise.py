import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

files = ['x_25_80_60', 'x_30_90_70', 'x_60_80_60', 'x_95_110_70',
         'y_25_80_60', 'y_30_90_70', 'y_60_80_60', 'y_95_110_70']
c = 7

for filename in files:
    data = np.loadtxt(filename)
    filter_data = savgol_filter(data[:, 2], 3, 2)
    grad = np.gradient(filter_data)
    for i in range(len(grad)):
        if (grad[i:i+c] > 0).all():
            low_limit = i
            break
    for i in reversed(range(len(grad))):
        if (grad[i-c:i]< 0).all():
            high_limit = i
            break
    data = data[low_limit:high_limit+1]
    data[:, 2] = data[:, 2] - min(data[:, 2])
    np.savetxt('results/%s' % filename, data)
    plt.plot(filter_data)
    plt.plot(data[:, 2])
    plt.show()


