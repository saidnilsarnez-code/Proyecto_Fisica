import numpy as np
import matplotlib.pyplot as plt
archivo = "datos_csv.txt"  

data = np.loadtxt(archivo)


t = data[:, 0]
x = data[:, 1]
y = data[:, 2]



plt.figure(figsize=(8, 5))


plt.plot(t, x, marker="o", label="x(t)")


plt.plot(t, y, marker="s", label="y(t)")

plt.xlabel("t")
plt.ylabel("Valores")
plt.title("Gráficos de x(t) y y(t)")
plt.grid(True)
plt.legend()

plt.show()
