import pandas as pd
import time
import numpy as np
import sensormotion as sm
from  matplotlib import pyplot as plt
# parser = SylkParser("data/Excel.slk-20200706T152908Z-001/Excel.slk/SARA- Zebris Gait Sumer.slk")
star = time.time()
filename = '../data/Foot_Sensors_Deneme_Earthbased/Zebris-Ankle-FootSensorsDenemeEarthbased/Zebris_Ankle_Earthbased_5.xlsx'
df = pd.read_excel(filename,skiprows=3)

# df = pd.read_excel('../data/earth_based_sensordata/Sumer_Ankle_Lateral (Earth-Based).xlsx',skiprows=3)
Time_S  = df['Time,s'].to_numpy()
fig_size = (10, 3)
min_val = 0.75
min_dist = 55 # Distance between step
distance = 440 # Total Distance covered
Foot_Accel_Sensor_X_RT = df[['Foot Accel Earth X RT,mG']].to_numpy()
Foot_Accel_Sensor_Y_RT = df[['Foot Accel Earth Y RT,mG']].to_numpy()
Foot_Accel_Sensor_Z_RT = df[['Foot Accel Earth Z RT,mG']].to_numpy()

# plt.plot(Foot_Accel_Sensor_Y_RT)
# plt.show()
f, axarr1 = plt.subplots(1, 1, figsize=fig_size)
axarr1.plot(Time_S, Foot_Accel_Sensor_Y_RT, "k")
plt.xlim(xmin=0)

axarr1.grid(True)

f.subplots_adjust(hspace=0.5)

Foot_Accel_Sensor_Y_RT = Foot_Accel_Sensor_Y_RT.T
Foot_Accel_Sensor_X_RT = Foot_Accel_Sensor_X_RT.T
Foot_Accel_Sensor_Z_RT = Foot_Accel_Sensor_Z_RT.T


b, a = sm.signal.build_filter(frequency=15,#[2,15],
                              sample_rate=100,
                              filter_type='low',
                              filter_order=2)
x_filtered = sm.signal.filter_signal(b, a, signal=Foot_Accel_Sensor_X_RT)
y_filtered = sm.signal.filter_signal(b, a, signal=Foot_Accel_Sensor_Y_RT)
z_filtered = sm.signal.filter_signal(b, a, signal=Foot_Accel_Sensor_Z_RT)

# peak_times_x, peak_values_x = sm.peak.find_peaks(time=Time_S, signal=x_filtered[0],
#                                              peak_type='valley',
#                                              min_val=0.55, min_dist=15,
#                                              plot=False)
peak_times_y, peak_values_y = sm.peak.find_peaks(time=Time_S, signal=y_filtered[0],
                                             peak_type='valley',
                                             min_val=min_val, min_dist=min_dist,
                                             plot=True)
# peak_times_z, peak_values_z = sm.peak.find_peaks(time=Time_S, signal=z_filtered[0],
#                                              peak_type='valley',
#                                              min_val=0.55, min_dist=15,
#                                              plot=False)

# cadence_x = sm.gait.cadence(time=Time_S, peak_times=peak_times_x, time_units='s')
# step_mean_x, step_sd_x, step_cov_x = sm.gait.step_time(peak_times=peak_times_x)
# print('X = ',cadence_x,step_mean_x,step_sd_x,step_cov_x)

cadence_y = sm.gait.cadence(time=Time_S, peak_times=peak_times_y, time_units='s')
step_time_diff_y,step_time_y, step_time_sd_y, step_time_cov_y = sm.gait.step_time(peak_times=peak_times_y)
# print('Y = ',cadence_y,step_mean_y,step_sd_y,step_cov_y)
step_count = sm.gait.step_count(peak_times_y)
print(' - Number of steps: {}'.format(step_count))
print(' - Cadence: {:.2f} steps/min'.format(cadence_y))
print(' - Mean step time: {:.2f}ms'.format(step_time_y*distance))
# print(' - All step time Diff: {} '.format(step_time_diff_y))
print(' - Step time variability (standard deviation): {:.2f}'.format(step_time_sd_y))
print(' - Step time variability (coefficient of variation): {:.2f}'.format(step_time_cov_y))
# print(' - Gait Velocity: {}'.format((cadence_y*60/distance)*distance/3600))
print(' - Gait Velocity: {}'.format((cadence_y*distance)/120)) # Formula needs to be adjusted. Its wrong at the moment.

# cadence_z = sm.gait.cadence(time=Time_S, peak_times=peak_times_z, time_units='s')
# step_mean_z, step_sd_z, step_cov_z = sm.gait.step_time(peak_times=peak_times_z)
# print('Z = ',cadence_z,step_mean_z,step_sd_z,step_cov_z)

# Foot_Accel_Sensor_X_RT = df[['Foot Accel Earth X LT,mG']].to_numpy()
Foot_Accel_Sensor_Y_RT = df[['Foot Accel Earth Y LT,mG']].to_numpy()
# Foot_Accel_Sensor_Z_RT = df[['Foot Accel Earth Z LT,mG']].to_numpy()
# plt.plot(Foot_Accel_Sensor_Y_RT)
# plt.show()
f, axarr = plt.subplots(1, 1, figsize=fig_size)
axarr.plot(Time_S, Foot_Accel_Sensor_Y_RT, "k")
plt.xlim(xmin=0)
axarr.grid(True)

f.subplots_adjust(hspace=0.5)

Foot_Accel_Sensor_Y_RT = Foot_Accel_Sensor_Y_RT.T
# Foot_Accel_Sensor_X_RT = Foot_Accel_Sensor_X_RT.T
# Foot_Accel_Sensor_Z_RT = Foot_Accel_Sensor_Z_RT.T


# x_filtered = sm.signal.filter_signal(b, a, signal=Foot_Accel_Sensor_X_RT)
y_filtered = sm.signal.filter_signal(b, a, signal=Foot_Accel_Sensor_Y_RT)
# z_filtered = sm.signal.filter_signal(b, a, signal=Foot_Accel_Sensor_Z_RT)

# peak_times_x, peak_values_x = sm.peak.find_peaks(time=Time_S, signal=x_filtered[0],
#                                              peak_type='valley',
#                                              min_val=0.55, min_dist=15,
#                                              plot=False)
peak_times_y, peak_values_y = sm.peak.find_peaks(time=Time_S, signal=y_filtered[0],
                                             peak_type='valley',
                                             min_val=min_val, min_dist=min_dist,
                                             plot=True)
# peak_times_z, peak_values_z = sm.peak.find_peaks(time=Time_S, signal=z_filtered[0],
#                                              peak_type='valley',
#                                              min_val=0.55, min_dist=15,
#                                              plot=False)

# cadence_x = sm.gait.cadence(time=Time_S, peak_times=peak_times_x, time_units='s')
# step_mean_x, step_sd_x, step_cov_x = sm.gait.step_time(peak_times=peak_times_x)
# print('X = ',cadence_x,step_mean_x,step_sd_x,step_cov_x)

cadence_y = sm.gait.cadence(time=Time_S, peak_times=peak_times_y, time_units='s')
step_time_diff_y,step_time_y, step_time_sd_y, step_time_cov_y = sm.gait.step_time(peak_times=peak_times_y)
# print('Y = ',cadence_y,step_mean_y,step_sd_y,step_cov_y)
step_count = sm.gait.step_count(peak_times_y)
print('========================================')
print('========================================')
print(' - Number of steps: {}'.format(step_count))
print(' - Cadence: {:.2f} steps/min'.format(cadence_y))
print(' - Mean step time: {:.2f}ms'.format(step_time_y*distance))
# print(' - All step time Diff: {} '.format(step_time_diff_y))
print(' - Step time variability (standard deviation): {:.2f}'.format(step_time_sd_y))
print(' - Step time variability (coefficient of variation): {:.2f}'.format(step_time_cov_y))
print(' - Gait Velocity: {}'.format((cadence_y*distance)/120)) # Formula needs to be adjusted. Its wrong at the moment.

plt.show()
