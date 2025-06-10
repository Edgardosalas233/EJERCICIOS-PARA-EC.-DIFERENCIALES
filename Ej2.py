import matplotlib.pyplot as plt

# Parámetros físicos
g = 9.81
k = 0.05  # kg/m
m = 5     # kg

# Ecuación diferencial: dv/dt = -g + (k/m) * v^2
def f(t, v):
    return -g + (k / m) * v**2

# Método de Euler
def euler(f, t0, v0, h, n):
    t, v = [t0], [v0]
    for _ in range(n):
        v0 += h * f(t0, v0)
        t0 += h
        t.append(t0)
        v.append(v0)
    return t, v

# Método de Heun
def heun(f, t0, v0, h, n):
    t, v = [t0], [v0]
    for _ in range(n):
        k1 = f(t0, v0)
        k2 = f(t0 + h, v0 + h * k1)
        v0 += h * (k1 + k2) / 2
        t0 += h
        t.append(t0)
        v.append(v0)
    return t, v

# Método de Runge-Kutta 4
def rk4(f, t0, v0, h, n):
    t, v = [t0], [v0]
    for _ in range(n):
        k1 = f(t0, v0)
        k2 = f(t0 + h/2, v0 + h*k1/2)
        k3 = f(t0 + h/2, v0 + h*k2/2)
        k4 = f(t0 + h, v0 + h*k3)
        v0 += h * (k1 + 2*k2 + 2*k3 + k4) / 6
        t0 += h
        t.append(t0)
        v.append(v0)
    return t, v

# Condiciones iniciales y parámetros
t0 = 0
v0 = 0
h = 0.1          # paso
t_max = 15
n = int((t_max - t0) / h)

# Ejecutar métodos
te, ve = euler(f, t0, v0, h, n)
th, vh = heun(f, t0, v0, h, n)
tr, vr = rk4(f, t0, v0, h, n)

# Mostrar resultados finales
print("RESULTADOS FINALES - EJERCICIO (m=5kg, k=0.05):")
print(f"Euler:        v({te[-1]:.2f}) = {ve[-1]:.4f} m/s")
print(f"Heun:         v({th[-1]:.2f}) = {vh[-1]:.4f} m/s")
print(f"Runge-Kutta:  v({tr[-1]:.2f}) = {vr[-1]:.4f} m/s")

# Graficar
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(te, ve, 'r', label='Euler')
plt.title('Método de Euler')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(th, vh, 'g', label='Heun')
plt.title('Método de Heun')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(tr, vr, 'b', label='Runge-Kutta 4')
plt.title('Método de Runge-Kutta 4° Orden')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.grid(True)

plt.tight_layout()
plt.show()
