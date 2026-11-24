import numpy as np
import matplotlib.pyplot as plt

mc2 = 940
hbarc = 197.3
k = 100
b_values = [0, 10, 30]

r_max = 5
N = 500

r = np.linspace(0, r_max, N + 2)[1:-1]
dr = r[1] - r[0]


k = hbarc**2 / (2 * mc2 * dr**2)

plt.figure(figsize=(9, 5))


for b in b_values:

   
    V = 0.5 * k * r**2 + (1/3) * b * r**3

    
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

    print("For b =", b, "MeV/fm^3")
    print("Ground state energy =", round(E, 3), "MeV")
    print()

   
    plt.plot(r, u, label="b = " + str(b))

plt.xlabel("Distance r (fm)")
plt.ylabel("Wavefunction u(r)")
plt.title("Anharmonic Oscillator Ground State")

plt.legend()
plt.grid()

plt.show()

