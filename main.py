import signal
import sys
import matplotlib.pyplot as plt
import numpy as np


def interrupt_handler(sig, frame):  # noqa
    print('\n\n Keyboard Interrupt Received. Exiting program...')
    sys.exit(0)


signal.signal(signal.SIGINT, interrupt_handler)

print(' Press ENTER to use default values.')
launch_speed = input(' Provide an initial speed in m/s (Default: 30) > ') or 30
elevation_angle = input(' Provide an initial elevation angle in degrees (Default: 45) > ') or 45
azimuth_angle = input(' Provide an initial azimuth angle in degrees (Default: 0) > ') or 0

# Variables of the equation
g = 9.81
t = np.linspace(0, 10, 1000)
v_0 = float(launch_speed)
r_elev = np.radians(float(elevation_angle))
r_azim = np.radians(float(azimuth_angle))

while True:
    offset_values = input(' Provide the starting position in x,y,z form (Default: 0,0,0) > ') or '0,0,0'
    try:
        offset = offset_values.split(',')
        x_off = float(offset[0])
        y_off = float(offset[1])
        z_off = float(offset[2])
        break
    except IndexError:
        print(''' ERROR - Provided values are invalid.
 Make sure to give your values in "NUMBER,NUMBER,NUMBER" form
''')

# Calculation of values of each axis as a function of time (t) for plotting
x = ((v_0 * np.cos(r_elev) * np.cos(r_azim)) * t) + x_off
y = ((v_0 * np.sin(r_elev) * np.cos(r_azim)) * t - 0.5 * g * t ** 2) + y_off
z = ((v_0 * np.sin(r_elev) * np.sin(r_azim)) * t) + z_off

print(v_0, elevation_angle, r_elev, azimuth_angle, r_azim, (v_0 * np.cos(r_elev)) * 0.75, np.sin(r_azim), np.cos(r_azim)) # noqa

# Filter out values y < 0
mask = y >= 0
x = x[mask]
y = y[mask]
z = z[mask]

for column_x, column_y, column_z in zip(x, y, z):
    print(column_x, column_y, column_z)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, z, y)
ax.set_xlabel('X')
ax.set_ylabel('Z')
ax.set_zlabel('Y')
plt.show()
