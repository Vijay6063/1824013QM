import numpy as np
import matplotlib.pyplot as plt

mc2 = 940 * 10**6
hbarc = 1973
D = 0.7555001
a = 1.44
r0 = 0.131349

r_max = 1.0
N = 500

r = np.linspace(0.001, r_max, N + 2)[1:-1]
dr = r[1] - r[0]


r_prime = (r - r0) / r0
V = D * (np.exp(-2*a*r_prime) - np.exp(-a*r_prime))


t = hbarc**2 / (2 * mc2 * dr**2)


H = np.zeros((N, N))

for i in range(N):

    H[i, i] = 2*t + V[i]

    if i > 0:
        H[i, i-1] = -t

    if i < N-1:
        H[i, i+1] = -t


energy, wave = np.linalg.eigh(H)


E = energy[0]
u = wave[:, 0]

u = u / np.sqrt(np.sum(u**2) * dr)

print("Lowest vibrational energy =", round(E, 6), "eV")


plt.figure(figsize=(9, 5))

plt.plot(r, u)

plt.xlabel("Distance r (Angstrom)")
plt.ylabel("Wavefunction u(r)")
plt.title("Ground State Wavefunction for Morse Potential")

plt.grid()

plt.show()