import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)
theta = np.radians(60)  # Angle in radians
nu = 0.1 # Kinematic viscosity (m^2/s)
h = 0.323  # Channel height (m)

# Velocity profile function
def velocity_profile(y, g=9.8, theta=np.radians(90), nu=5.0e-1, h=0.5):
    return (g * np.sin(theta) / nu) * y * (h - y / 2)

#a, b = 0, 0.5
#integral, error = quad(velocity_profile, a, b)

# Create an array of y values from 0 to h
y_values = np.linspace(0, h, 100)
u_values = velocity_profile(y_values, g, theta, nu, h)

# Plot the velocity profile
plt.figure(figsize=(10, 6))
plt.plot(y_values, u_values, label='Velocity Profile')
plt.ylabel('Velocity (u) [m/s]')
plt.xlabel('Height (y) [m]')
plt.title('Velocity Profile in a Channel')
plt.legend()
plt.grid(True)
plt.show()