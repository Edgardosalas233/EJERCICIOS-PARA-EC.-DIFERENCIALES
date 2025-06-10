import numpy as np
import matplotlib.pyplot as plt

# Parámetros del modelo
alpha = 0.8     # tasa de crecimiento
k = 60          # capacidad de carga
v = 0.25        # exponente
A0 = 1          # área inicial del tumor (mm²)
t0 = 0          # tiempo inicial (días)
tf = 30         # tiempo final (días)
h = 1           # paso
n = int((tf - t0) / h)  # número de pasos

# EDO: dA/dt = alpha * A * (1 - (A/k)^v)
def f(t, A):
    return alpha * A * (1 - (A / k)**v)

# Método de Euler
def euler(f, t0, A0, h, n):
    t = [t0]
    A = [A0]
    for _ in range(n):
        A0 += h * f(t0, A0)
        t0 += h
        t.append(t0)
        A.append(A0)
    return t, A

# Método de Heun
def heun(f, t0, A0, h, n):
    t = [t0]
    A = [A0]
    for _ in range(n):
        k1 = f(t0, A0)
        k2 = f(t0 + h, A0 + h * k1)
        A0 += (h / 2) * (k1 + k2)
        t0 += h
        t.append(t0)
        A.append(A0)
    return t, A

# Método de Runge-Kutta 4
def rk4(f, t0, A0, h, n):
    t = [t0]
    A = [A0]
    for _ in range(n):
        k1 = f(t0, A0)
        k2 = f(t0 + h / 2, A0 + h * k1 / 2)
        k3 = f(t0 + h / 2, A0 + h * k2 / 2)
        k4 = f(t0 + h, A0 + h * k3)
        A0 += (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
        t0 += h
        t.append(t0)
        A.append(A0)
    return t, A

# Resolver con cada método
te, Ae = euler(f, t0, A0, h, n)
th, Ah = heun(f, t0, A0, h, n)
tr, Ar = rk4(f, t0, A0, h, n)

# Imprimir resultados finales
print("RESULTADOS FINALES - EJERCICIO 1 (Área del tumor en mm² al día 30):")
print(f"Euler:        A({te[-1]} días) = {Ae[-1]:.4f} mm²")
print(f"Heun:         A({th[-1]} días) = {Ah[-1]:.4f} mm²")
print(f"Runge-Kutta:  A({tr[-1]} días) = {Ar[-1]:.4f} mm²")

# Graficar por separado

# Gráfica 1: Euler
plt.figure(figsize=(8, 4))
plt.plot(te, Ae, 'r-', label='Euler')
plt.title('Método de Euler - Área del tumor')
plt.xlabel('Tiempo (días)')
plt.ylabel('Área (mm²)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Gráfica 2: Heun
plt.figure(figsize=(8, 4))
plt.plot(th, Ah, 'g--', label='Heun')
plt.title('Método de Heun - Área del tumor')
plt.xlabel('Tiempo (días)')
plt.ylabel('Área (mm²)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Gráfica 3: Runge-Kutta 4
plt.figure(figsize=(8, 4))
plt.plot(tr, Ar, 'b-.', label='Runge-Kutta 4')
plt.title('Método de Runge-Kutta 4° Orden - Área del tumor')
plt.xlabel('Tiempo (días)')
plt.ylabel('Área (mm²)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
