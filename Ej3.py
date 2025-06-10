import matplotlib.pyplot as plt

# Parámetros del problema
k = 0.000095     # constante (1/año)
N_M = 5000       # límite de población
N0 = 100         # población inicial
t0 = 0           # tiempo inicial
tf = 20          # tiempo final (años)
h = 0.5          # paso de tiempo
n = int((tf - t0) / h)  # número de pasos

# Función diferencial: dN/dt = k*N*(N_M - N)
def f(t, N):
    return k * N * (N_M - N)

# Método de Euler
def euler(f, t0, N0, h, n):
    t = [t0]
    N = [N0]
    for _ in range(n):
        N0 += h * f(t0, N0)
        t0 += h
        t.append(t0)
        N.append(N0)
    return t, N

# Método de Heun
def heun(f, t0, N0, h, n):
    t = [t0]
    N = [N0]
    for _ in range(n):
        k1 = f(t0, N0)
        k2 = f(t0 + h, N0 + h * k1)
        N0 += (h / 2) * (k1 + k2)
        t0 += h
        t.append(t0)
        N.append(N0)
    return t, N

# Método de Runge-Kutta de 4to orden
def rk4(f, t0, N0, h, n):
    t = [t0]
    N = [N0]
    for _ in range(n):
        k1 = f(t0, N0)
        k2 = f(t0 + h/2, N0 + h * k1 / 2)
        k3 = f(t0 + h/2, N0 + h * k2 / 2)
        k4 = f(t0 + h, N0 + h * k3)
        N0 += (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
        t0 += h
        t.append(t0)
        N.append(N0)
    return t, N

# Ejecutar los métodos
te, Ne = euler(f, t0, N0, h, n)
th, Nh = heun(f, t0, N0, h, n)
tr, Nr = rk4(f, t0, N0, h, n)

# Imprimir resultados finales
print("RESULTADOS FINALES - EJERCICIO 3:")
print(f"Euler:        N({te[-1]:.2f}) = {Ne[-1]:.4f}")
print(f"Heun:         N({th[-1]:.2f}) = {Nh[-1]:.4f}")
print(f"Runge-Kutta:  N({tr[-1]:.2f}) = {Nr[-1]:.4f}")

# Gráficas individuales
plt.figure(figsize=(12, 9))

plt.subplot(3, 1, 1)
plt.plot(te, Ne, 'r', label='Euler')
plt.title('Método de Euler - Ejercicio 3')
plt.xlabel('Tiempo (años)')
plt.ylabel('Población')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(th, Nh, 'g', label='Heun')
plt.title('Método de Heun - Ejercicio 3')
plt.xlabel('Tiempo (años)')
plt.ylabel('Población')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(tr, Nr, 'b', label='Runge-Kutta 4')
plt.title('Método de Runge-Kutta 4° Orden - Ejercicio 3')
plt.xlabel('Tiempo (años)')
plt.ylabel('Población')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
