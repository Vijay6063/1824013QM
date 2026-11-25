import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2*np.pi, 100)

theta, phi = np.meshgrid(theta, phi)

values = [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2)]

fig = plt.figure(figsize=(12, 8))

for i, (l, m) in enumerate(values):

    if l == 0:
        Y = np.ones_like(theta) / np.sqrt(4*np.pi)

    elif l == 1 and m == 0:
        Y = np.sqrt(3/(4*np.pi)) * np.cos(theta)

    elif l == 1 and m == 1:
        Y = np.sqrt(3/(4*np.pi)) * np.sin(theta)

    elif l == 2 and m == 0:
        Y = np.sqrt(5/(16*np.pi)) * (3*np.cos(theta)**2 - 1)

    elif l == 2 and m == 1:
        Y = np.sqrt(15/(4*np.pi)) * np.sin(theta) * np.cos(theta)

    elif l == 2 and m == 2:
        Y = np.sqrt(15/(16*np.pi)) * np.sin(theta)**2

    P = np.abs(Y)**2

    x = P * np.sin(theta) * np.cos(phi)
    y = P * np.sin(theta) * np.sin(phi)
    z = P * np.cos(theta)

    ax = fig.add_subplot(2, 3, i+1, projection='3d')

    ax.plot_surface(x, y, z)

    ax.set_title("l = " + str(l) + ", m = " + str(m))

plt.tight_layout()
plt.show()