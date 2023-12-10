import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
# matplotlib.use('Qt5Agg')


def main():
    fnames_4hz = ['AIO0-4hz.txt', 'AIO1-4hz.txt']
    fnames_1hz = ['AIO0_1Hz.txt', 'AIO1_1Hz.txt']
    data_4hz = [np.genfromtxt(file_path, delimiter=',')
                for file_path in fnames_4hz]
    data_1hz = [np.genfromtxt(file_path, delimiter=',')
                for file_path in fnames_1hz]

    endpoint = 700  # Until which index we want to plot data
    # v1_4hz = data_4hz[1][1] - data_4hz[0]
    sampling_freq = 48 * 1e6  # Hz
    time = np.arange(len(data_1hz[1])) * (1/sampling_freq)
    v1_1hz = data_1hz[1] - data_1hz[0]
    vtot = 5  # Vs provided by Labjack
    # v2_4hz = vtot - v1_4hz
    v2_1hz = vtot - v1_1hz
    r = 1e3  # resistance value
    r_timeseries_1hz = (10 * r * v1_1hz) / v2_1hz
    print(time)
    plt.figure(figsize=(40, 5))
    plt.plot(time, r_timeseries_1hz)
    plt.title('Resistance Timeseries (Ohm)')
    plt.show()


if __name__ == '__main__':
    main()
