# Constants
u = 4  # Average velocity of the flow (m/s)
b = 0.2  # Width of the channel (m)
h = 1  # Depth of the flow (m)
nu = 5.0e-2  # Kinematic viscosity of the fluid (m^2/s)

# Calculate cross-sectional area and wetted perimeter
A = b * h  # Cross-sectional area (m^2)
P = b + 2 * h  # Wetted perimeter (m)

# Calculate hydraulic radius
Rh = A / P

# Calculate Reynolds number
Re = (u * Rh) / nu

print(f"Reynolds Number for the open channel: {Re:.2f}")