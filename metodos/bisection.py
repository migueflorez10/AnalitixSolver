import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Define la función para la cual deseamos encontrar la raíz
def func(x):
    return x ** 2 - 4

# Implementación del método de bisección
def bisection(f, a, b, tol):
    if f(a) * f(b) >= 0:
        print("Error: La función debe tener signos opuestos en los extremos del intervalo.")
        return None

    results = []  # Para almacenar los resultados de cada paso
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        results.append((a, b, c, f(c)))
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    # Crear un DataFrame y guardarlo en un archivo de texto
    df = pd.DataFrame(results, columns=['a', 'b', 'Midpoint', 'f(Midpoint)'])
    df.to_csv('bisection_results.txt', sep='\t', index=False)
    
    # Graficar la función y la aproximación de la raíz
    x = np.linspace(a - 1, b + 1, 400)
    y = f(x)
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='f(x)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(x=c, color='red', linestyle='--', label='Aproximación de la raíz')
    plt.title('Método de Bisección')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.savefig('bisection_plot.png')
    plt.show()

    return c

# Entradas del usuario
a = float(input("Ingrese el límite inferior a: "))
b = float(input("Ingrese el límite superior b: "))
tol = float(input("Ingrese la tolerancia tol: "))

# Llamar al método de bisección
root = bisection(func, a, b, tol)
print(f"La raíz aproximada es: {root}")
