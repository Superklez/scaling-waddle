import numpy as np
import matplotlib.pyplot as plt

Nx = 101
Nt = 100000
Dx = 0.03   # diverges at 0.015
Dt = 0.15    # diverges at 4.65

kappa = 237 # conductivity
c = 900     # specific heat
rho = 2700  # density

T = np.zeros((Nx, 3))
Tpl = np.zeros((Nx, 201))

T[1:-1, 0] = 100
T[1:-1, 1] = 100
T[0, 0] = 0; T[-1, 0] = 0    # redundant
T[0, 1] = 0; T[-1, 1] = 0    # redundant
T[0, 2] = 0; T[-1, 2] = 0    # redundant

eta = 2 * kappa / (c * rho) * Dt / (Dx * Dx)
#print(eta)  # diverges if eta > 0.5

m = 1
for t in range(1, Nt):
    T[1:-1, 2] = T[1:-1, 1] + eta * (T[2:, 1] + T[:-2, 1] - 2 * T[1:-1, 1])
    if t == 1 or t % 500 == 0:
        Tpl[1:-1:2, m] = T[1:-1:2, 2]
        m += 1
    T[1:-1, 0] = T[1:-1, 1]
    T[1:-1, 1] = T[1:-1, 2]

y = list(range(1, 200))
x = list(range(1, Nx-1, 2))
X, Y = np.meshgrid(x, y)

Z = Tpl[X, Y]

fig = plt.figure(figsize=(10, 10), dpi=100)
ax = plt.axes(projection ='3d')
ax.plot_wireframe(X, Y, Z, color='royalblue')
ax.view_init(30, 45)
ax.set_xlabel('Position')
ax.set_ylabel('Time')
ax.set_zlabel('Temperature')
plt.show()
