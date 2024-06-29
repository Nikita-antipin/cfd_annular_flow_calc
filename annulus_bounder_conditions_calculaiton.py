from client import open_test_data

import math

def calculate_annulus_area(D_o, D_i):
    # Calculate the radii
    R_o = D_o / 2
    R_i = D_i / 2

    # Calculate the area of the outer and inner circles
    area_outer = math.pi * (R_o ** 2)
    area_inner = math.pi * (R_i ** 2)

    # Calculate the annulus area
    annulus_area = area_outer - area_inner

    return annulus_area

def calculate_initial_conditions(Re, U, L):
    # Constants
    c_mu = 0.09

    # Calculate turbulence intensity I
    I = 0.16 * Re ** (-1 / 8)

    # Calculate turbulent kinetic energy k
    k = 3 / 2 * (U * I) ** 2

    # Calculate turbulent length scale l
    l = 0.07 * L

    # Calculate dissipation rate epsilon
    epsilon = (c_mu ** (3 / 4)) * (k ** (3 / 2)) * (l ** -1)

    return I, k, epsilon

def calculate_reynolds_annular(D_o, D_i, U, rho, mu):
    # Calculate hydraulic diameter
    D_h = D_o - D_i

    # Calculate Reynolds number
    Re = (rho * U * D_h) / mu

    return Re

# Example inputs
D_o = 0.0762
D_i = 0.0422

area_total = calculate_annulus_area(D_o, D_i)

D_i_water = 0.0662
D_o_water = 0.0522

caetano_tests = open_test_data("caetano/water.json")
caetano_tests_num = len(caetano_tests)

#water-air:
#annular 0 - 11 (6 - 11) in brackests there are cases with gradient
#bubble: 12 - 34 (12 - 15, 16 - 24)
#dispersed: 35 - 48 (35, 36, 45 - 48)
#slug 49 - 89 (77 - 89)

qg_rc_m3day, ql_rc_m3day, fact_h_l, fact_dp_dl, fact_pattern = caetano_tests[77]



area1_water = calculate_annulus_area(D_o, D_i_water)
area2_water = calculate_annulus_area(D_o_water, D_i)
area_air = calculate_annulus_area(D_i_water, D_o_water)

us_water = ql_rc_m3day / area_total
u_water = us_water * area_total / (area1_water + area2_water)
u_water1 = u_water
u_water2 = u_water

print("Для воды вводить:", "   u_water1 - ",u_water1, "   u_water2 - ",u_water2)

us_air = qg_rc_m3day / area_total
u_air = us_air * area_total / area_air

print("Для воздуха вводить:   ", u_air)

rho_water = 1000
rho_air = 4
mu_water = 1.76e-6
mu_air = 1.849e-5

# Calculate Reynolds number for annular space
Re_water1 = calculate_reynolds_annular(D_o, D_i_water, u_water1, rho_water, mu_water)
Re_water2 = calculate_reynolds_annular(D_o_water, D_i, u_water2, rho_water, mu_water)


Re_air = calculate_reynolds_annular(D_i_water, D_o_water, u_air, rho_air, mu_air)


# Calculate characteristic length (hydraulic diameter)
L_water1 = D_o - D_i_water
L_water2 = D_o_water - D_i
L_air = D_i_water - D_o_water

# Calculate initial conditions
I_water1, k_water1, epsilon_water1 = calculate_initial_conditions(Re_water1, u_water1, L_water1)

print("k_water1:", k_water1, "   epsilon_water1:", epsilon_water1)

I_water2, k_water2, epsilon_water2 = calculate_initial_conditions(Re_water2, u_water2, L_water2)

print("k_water2:", k_water2, "   epsilon_water2:", epsilon_water2)

I_air, k_air, epsilon_air = calculate_initial_conditions(Re_air, u_air, L_air)

print("k_air:", k_air, "   epsilon_air:", epsilon_air)
