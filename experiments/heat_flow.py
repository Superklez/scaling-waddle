import numpy as np
import matplotlib.pyplot as plt

Nx = 101
Nt = 15000
Dx = 0.03
Dt = 1.5

kappa = 237 # conductivity
C = 900     # specific heat
rho = 2700  # density

T = np.zeros((2, Nx))
Tpl = np.zeros((31, Nx))

T[0, 1:-1] = 100
#T[0, 0] = 0; T[0, 1] = 0    # redundant
#T[-1, 0] = 0; T[-1, 1] = 0  # redundant

const = kappa / (C * rho) * Dt / (Dx * Dx)

m = 1
for t in range(1, Nt):
    T[1, 1:-1] = T[0, 1:-1] + const * (T[0, 2:] + T[0, :-2] - 2 * T[0, 1:-1])
    if t == 1 or t % 500 == 0:
        Tpl[m, 1:-1:2] = T[1, 1:-1:2]
        m += 1
    T[0, 1:-1] = T[1, 1:-1]

x = list(range(1, Nx-1, 2))
y = list(range(1, 30))
X, Y = np.meshgrid(x, y)

Z = Tpl[Y, X]

fig = plt.figure(figsize=(10, 10), dpi=100)
ax = plt.axes(projection ='3d')
ax.plot_wireframe(X, Y, Z, color='royalblue')
ax.view_init(30, 45)
ax.set_xlabel('Position')
ax.set_ylabel('Time')
ax.set_zlabel('Temperature')
plt.show()
