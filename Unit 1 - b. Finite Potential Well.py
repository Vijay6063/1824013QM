import numpy as np
import matplotlib.pyplot as plt

V0 = 20
a = 2

E_values = np.linspace(0.001, V0 - 0.001, 2000)


def even(E):
    k = np.sqrt(E)
    alpha = np.sqrt(V0 - E)
    return k * np.sin(k * a) - alpha * np.cos(k * a)

def odd(E):
    k = np.sqrt(E)
    alpha = np.sqrt(V0 - E)
    return k * np.cos(k * a) + alpha * np.sin(k * a)

def find_root(func, x1, x2):
    for i in range(100):
        xm = (x1 + x2) / 2

        if func(x1) * func(xm) < 0:
            x2 = xm
        else:
            x1 = xm

    return (x1 + x2) / 2


energies = []

for func in [even, odd]:
    for i in range(len(E_values) - 1):
        x1 = E_values[i]
        x2 = E_values[i + 1]

        if func(x1) * func(x2) < 0:
            E = find_root(func, x1, x2)

            if not any(abs(E - old) < 0.01 for old in energies):
                energies.append(E)

energies.sort()


x = np.linspace(-5 * a, 5 * a, 2000)
V = np.where(abs(x) <= a, 0, V0)

plt.figure(figsize=(10, 6))
plt.plot(x, V, color='black', label="Potential")

for n, E in enumerate(energies):

    k = np.sqrt(E)
    alpha = np.sqrt(V0 - E)

    psi = np.zeros_like(x)

    if n % 2 == 0:
       
        psi_inside = np.cos(k * x)

        boundary = np.cos(k * a)

        psi_outside = boundary * np.exp(-alpha * (abs(x) - a))

        psi = np.where(abs(x) <= a, psi_inside, psi_outside)

    else:
       
        psi_inside = np.sin(k * x)

        boundary = np.sin(k * a)

        psi_outside = np.sign(x) * boundary * np.exp(-alpha * (abs(x) - a))

        psi = np.where(abs(x) <= a, psi_inside, psi_outside)

    
    norm = np.sqrt(np.trapz(psi**2, x))
    psi = psi / norm

    print("Energy level", n + 1, "=", round(E, 4))

    plt.plot(x, psi + E, label="E = " + str(round(E, 3)))

plt.xlabel("Position (x)")
plt.ylabel("Energy / Wavefunction")
plt.title("Finite Potential Well")
plt.legend()
plt.grid()
plt.show()