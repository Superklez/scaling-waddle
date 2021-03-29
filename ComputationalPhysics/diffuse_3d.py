import numpy as np
import matplotlib.pyplot as plt

def diffuse(atoms=400, t=100, T=300, xlims=(-15, 15), ylims=(-15, 15), zlims=(-15,15), nx=4, ny=4, nz=4, random_state=0):

    init_atoms = np.zeros((atoms, 3))
    diffused_atoms = np.zeros((atoms, 3))
    k = 1.38065e-23
    tol = k/(2*np.exp(1))

    gridx = np.linspace(xlims[0], xlims[1], nx)
    gridy = np.linspace(ylims[0], ylims[1], ny)
    gridz = np.linspace(zlims[0], zlims[1], nz)

    entropy_vals = []
    np.random.RandomState(random_state)

    for i in range(t):
        step = (2*np.random.random((atoms, 3)) - 1) * (T / 300)
        diffused_atoms[:, 0] += step[:, 0]
        diffused_atoms[:, 1] += step[:, 1]
        diffused_atoms[:, 2] += step[:, 2]

        a_temp = np.zeros(diffused_atoms[diffused_atoms[:, 0] <= xlims[0]].shape)
        a_temp[:, 1] = diffused_atoms[diffused_atoms[:, 0] <= xlims[0]][:, 1]
        a_temp[:, 2] = diffused_atoms[diffused_atoms[:, 0] <= xlims[0]][:, 2]
        a_temp[:, 0] = diffused_atoms[diffused_atoms[:, 0] <= xlims[0]][:, 0] + 2 * abs(xlims[0] - diffused_atoms[diffused_atoms[:, 0] <= xlims[0]][:, 0])
        diffused_atoms[diffused_atoms[:, 0] <= xlims[0]] = a_temp

        b_temp = np.zeros(diffused_atoms[diffused_atoms[:, 0] >= xlims[1]].shape)
        b_temp[:, 1] = diffused_atoms[diffused_atoms[:, 0] >= xlims[1]][:, 1]
        b_temp[:, 2] = diffused_atoms[diffused_atoms[:, 0] >= xlims[1]][:, 2]
        b_temp[:, 0] = diffused_atoms[diffused_atoms[:, 0] >= xlims[1]][:, 0] - 2 * abs(xlims[1] - diffused_atoms[diffused_atoms[:, 0] >= xlims[1]][:, 0])
        diffused_atoms[diffused_atoms[:, 0] >= xlims[1]] = b_temp

        c_temp = np.zeros(diffused_atoms[diffused_atoms[:, 1] <= ylims[0]].shape)
        c_temp[:, 0] = diffused_atoms[diffused_atoms[:, 1] <= ylims[0]][:, 0]
        c_temp[:, 2] = diffused_atoms[diffused_atoms[:, 1] <= ylims[0]][:, 2]
        c_temp[:, 1] = diffused_atoms[diffused_atoms[:, 1] <= ylims[0]][:, 1] + 2 * abs(ylims[0] - diffused_atoms[diffused_atoms[:, 1] <= ylims[0]][:, 1])
        diffused_atoms[diffused_atoms[:, 1] <= ylims[0]] = c_temp

        d_temp = np.zeros(diffused_atoms[diffused_atoms[:, 1] >= ylims[1]].shape)
        d_temp[:, 0] = diffused_atoms[diffused_atoms[:, 1] >= ylims[1]][:, 0]
        d_temp[:, 2] = diffused_atoms[diffused_atoms[:, 1] >= ylims[1]][:, 2]
        d_temp[:, 1] = diffused_atoms[diffused_atoms[:, 1] >= ylims[1]][:, 1] - 2 * abs(ylims[1] - diffused_atoms[diffused_atoms[:, 1] >= ylims[1]][:, 1])
        diffused_atoms[diffused_atoms[:, 1] >= ylims[1]] = d_temp

        e_temp = np.zeros(diffused_atoms[diffused_atoms[:, 2] <= zlims[0]].shape)
        e_temp[:, 0] = diffused_atoms[diffused_atoms[:, 2] <= zlims[0]][:, 0]
        e_temp[:, 1] = diffused_atoms[diffused_atoms[:, 2] <= zlims[0]][:, 1]
        e_temp[:, 2] = diffused_atoms[diffused_atoms[:, 2] <= zlims[0]][:, 2] + 2 * abs(zlims[0] - diffused_atoms[diffused_atoms[:, 2] <= zlims[0]][:, 2])
        diffused_atoms[diffused_atoms[:, 2] <= zlims[0]] = e_temp

        f_temp = np.zeros(diffused_atoms[diffused_atoms[:, 2] >= zlims[1]].shape)
        f_temp[:, 0] = diffused_atoms[diffused_atoms[:, 2] >= zlims[1]][:, 0]
        f_temp[:, 1] = diffused_atoms[diffused_atoms[:, 2] >= zlims[1]][:, 1]
        f_temp[:, 2] = diffused_atoms[diffused_atoms[:, 2] >= zlims[1]][:, 2] - 2 * abs(zlims[1] - diffused_atoms[diffused_atoms[:, 2] >= zlims[1]][:, 2])
        diffused_atoms[diffused_atoms[:, 2] >= zlims[1]] = f_temp

        temp_entropy_vals = []
        for i in range(len(gridx) - 1):
            for j in range(len(gridy) - 1):
                for k in range(len(gridz) - 1):
                    test_atoms = diffused_atoms[(gridx[i] < diffused_atoms[:, 0]) & (diffused_atoms[:, 0] < gridx[i+1]) &
                                                (gridy[j] < diffused_atoms[:, 1]) & (diffused_atoms[:, 1] < gridy[j+1]) &
                                                (gridz[k] < diffused_atoms[:, 2]) & (diffused_atoms[:, 2] < gridy[k+1])].shape[0]
                    P = test_atoms / atoms
                    if P == 0:
                        entropy = 0
                    else:
                        entropy = P * np.log(P)
                    temp_entropy_vals.append(entropy)

        temp_entropy_vals = -k * sum(temp_entropy_vals)
        entropy_vals.append(temp_entropy_vals)
    entropy_vals = np.array(entropy_vals)

    return diffused_atoms, entropy_vals

if __name__ == '__main__':
    xlims = (-9, 9)
    ylims = (-9, 9)
    zlims = (-9, 9)
    nx = 4
    ny = 4
    nz = 4
    gridx = np.linspace(xlims[0], xlims[1], nx)
    gridy = np.linspace(ylims[0], ylims[1], ny)
    gridz = np.linspace(zlims[0], zlims[1], nz)

    T = 300

    a, b = diffuse(atoms=10000, t=1000, T=T, xlims=xlims, ylims=ylims, zlims=zlims, nx=nx, ny=ny, nz=nz, random_state=0)

    fig = plt.figure(figsize=(10, 10), dpi=100)
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(a[:, 0], a[:, 1], a[:, 2], s=1)
    ax.set_xticks(gridx)
    ax.set_yticks(gridy)
    ax.set_zticks(gridz)
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z- Axis')
    plt.title(f'Position of diffused atoms for T={T}K')
    plt.show()
