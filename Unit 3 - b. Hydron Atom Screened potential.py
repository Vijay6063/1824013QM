import numpy as np
import matplotlib.pyplot as plt

e = 3.795
hbarc = 1973
m = 0.511 * 10**6

a_values = [3, 5, 7]

r_max = 30
N = 500

r = np.linspace(0, r_max, N + 2)[1:-1]
dr = r[1] - r[0]

k = (hbarc)**2 / (2 * m * dr**2)

plt.figure(figsize=(9, 5))


for a in a_values:

    
    V = -(e**2 / r) * np.exp(-r/a)

   
    H = np.zeros((N, N))

    for i in range(N):

        H[i, i] = 2*k + V[i]

        if i > 0:
            H[i, i-1] = -k

        if i < N-1:
            H[i, i+1] = -k

    
    energy, wave = np.linalg.eigh(H)

    
    E = energy[0]
    u = wave[:, 0]

   
    u = u / np.sqrt(np.sum(u**2) * dr)

    print("For a =", a, "Angstrom")
    print("Ground state energy =", round(E, 4), "eV")
    print()

    plt.plot(r, u, label="a = " + str(a) + " Angstrom")

plt.xlabel("Distance r (Angstrom)")
plt.ylabel("Radial Wavefunction u(r)")

plt.title("Ground State Wavefunction for Screened Coulomb Potential")

plt.legend()
plt.grid()

plt.show()