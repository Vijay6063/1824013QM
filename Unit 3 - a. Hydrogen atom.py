import numpy as np
import matplotlib.pyplot as plt

e = 3.795
hbarc = 1973
m = 0.511 * 10**6

r_max = 30
N = 500

r = np.linspace(0, r_max, N + 2)[1:-1]
dr = r[1] - r[0]

V = -(e**2) / r

k = (hbarc)**2 / (2 * m * dr**2)

H = np.zeros((N, N))

for i in range(N):
    H[i, i] = 2*k + V[i]

    if i > 0:
        H[i, i-1] = -k

    if i < N-1:
        H[i, i+1] = -k

energy, wave = np.linalg.eigh(H)

E1 = energy[0]
u1 = wave[:, 0]
E2 = energy[1]
u2 = wave[:, 1]
u1 = u1 / np.sqrt(np.sum(u1**2) * dr)
u2 = u2 / np.sqrt(np.sum(u2**2) * dr)

print("Ground state energy =", round(E1, 4), "eV")
print("First excited state energy =", round(E2, 4), "eV")


plt.figure(figsize=(9, 5))

plt.plot(r, u1, label="Ground State")
plt.plot(r, u2, label="First Excited State")

plt.xlabel("Distance r (Angstrom)")
plt.ylabel("Radial Wavefunction u(r)")
plt.title("Wavefunctions of Hydrogen Atom")

plt.legend()
plt.grid()
plt.show()
