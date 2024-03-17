def false_position(f, a, b, tol, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    results = []  # Para almacenar los resultados de cada iteración
    c = a  # Inicialmente establecemos c igual a a
    for iteration in range(max_iter):
        # Aplicar la fórmula de la regla falsa
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        results.append((a, b, c, f(c)))
        
        # Comprobar si hemos encontrado la raíz o si estamos lo suficientemente cerca
        if f(c) == 0 or abs(f(c)) < tol:
            break
        
        # Decidir el subintervalo en el que se encuentra la raíz
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    # Convertir los resultados en un DataFrame para facilitar la visualización y exportación
    results_df = pd.DataFrame(results, columns=['a', 'b', 'c', 'f(c)'])
    
    # Guardar los resultados en un archivo de texto
    results_df.to_csv('/mnt/data/false_position_results.txt', index=False, sep='\t')
    
    # Retornar el valor aproximado de la raíz y el DataFrame
    return c, results_df

# Definir la función para la cual se busca la raíz
def func(x):
    return x ** 2 - 4  # x^2 - 4 = 0 => x = ±2

# Parámetros para el método de regla falsa
a = -3  # Límite inferior del intervalo (debe tener un signo diferente al de b)
b = -1  # Límite superior del intervalo
tolerance = 1e-7  # Tolerancia para el criterio de parada

# Llamar al método de regla falsa
root, results_df = false_position(func, a, b, tolerance)
