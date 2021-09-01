import random
import numpy as np
import matplotlib.pyplot as plt

def main():
    init_atoms = 10000
    num_Bi_213 = init_atoms
    num_Po_213 = 0
    num_Tl_209 = 0
    num_Pb_209 = 0
    num_Bi_209 = 0

    # Bismuth-213: https://periodictable.com/Isotopes/083.213/index3.html
    # Polonium-213: https://periodictable.com/Isotopes/084.213/index3.html
    # Thallium-209: https://periodictable.com/Isotopes/081.209/index3.full.html
    # Lead-209: https://periodictable.com/Isotopes/082.209/index.p.full.html

    # Units below are in seconds
    tau_Bi_213 = 45.58333333333 * 60
    tau_Po_213 = 3.72 / 1e6
    tau_Tl_209 = 2.2 * 60
    tau_Pb_209 = 3.252777777778 * 60 * 60

    h = 1         # Time-step in seconds
    t_max = 20000 # Maximum time-steps

    # Probabilities of decay in one time-step
    p_Bi_213 = 1 - 2 ** (-h / tau_Bi_213)
    p_Po_213 = 1 - 2 ** (-h / tau_Po_213)
    p_Tl_209 = 1 - 2 ** (-h / tau_Tl_209)
    p_Pb_209 = 1 - 2 ** (-h / tau_Pb_209)

    # Lists to track the number of atoms
    t_points = np.arange(1, t_max + 1, h)
    Bi_213_points = []
    Po_213_points = []
    Tl_209_points = []
    Pb_209_points = []
    Bi_209_points = []

    # Decay chain of 213 Bi: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8143329/
    # Perform simulation on radioactive decay
    for t in t_points:
        Bi_213_points.append(num_Bi_213)
        Po_213_points.append(num_Po_213)
        Tl_209_points.append(num_Tl_209)
        Pb_209_points.append(num_Pb_209)
        Bi_209_points.append(num_Bi_209)

        decay_Pb_209 = np.sum(np.random.random(num_Pb_209) < p_Pb_209)
        num_Pb_209 -= decay_Pb_209
        num_Bi_209 += decay_Pb_209

        decay_Po_213 = np.sum(np.random.random(num_Po_213) < p_Po_213)
        num_Po_213 -= decay_Po_213
        num_Pb_209 += decay_Po_213

        decay_Tl_209 = np.sum(np.random.random(num_Tl_209) < p_Tl_209)
        num_Tl_209 -= decay_Tl_209
        num_Pb_209 += decay_Tl_209

        decay_Bi_213 = np.sum(np.random.random(num_Bi_213) < p_Bi_213)
        num_Bi_213 -= decay_Bi_213
        decay_to_Tl = np.sum(np.random.random(decay_Bi_213) < 0.0209)
        decay_to_Po = decay_Bi_213 - decay_to_Tl
        num_Tl_209 += decay_to_Tl
        num_Po_213 += decay_to_Po

    # Plot results
    fig, ax = plt.subplots(1, 1, figsize=(7, 5))

    ax.plot(t_points, Bi_213_points, label="Bismuth-213")
    ax.plot(t_points, Po_213_points, label="Polonium-213")
    ax.plot(t_points, Tl_209_points, label="Thallium-209")
    ax.plot(t_points, Pb_209_points, label="Lead-209")
    ax.plot(t_points, Bi_209_points, label="Bismuth-209")
    ax.grid(True)
    ax.set_xlabel("Time ($s$)")
    ax.set_ylabel("Number of atoms")
    plt.legend(loc="best")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()