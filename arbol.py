import numpy as np

# Parámetros
demanda_posible = [100, 200, 300]
probabilidades = [0.20, 0.50, 0.30]
pedidos = [100, 200, 300]

# Función de costo
def costo_total(q, d):
    compra = q*10 + 50
    almacen = max(q-d,0)*1
    faltante = max(d-q,0)*5
    return compra + almacen + faltante

# Simulación Monte Carlo
N = 100000  # número de iteraciones
resultados = {q: [] for q in pedidos}

for _ in range(N):
    d = np.random.choice(demanda_posible, p=probabilidades)
    for q in pedidos:
        resultados[q].append(costo_total(q,d))

# Costo esperado
for q in pedidos:
    print(f"Pedido {q}: costo esperado ≈ {np.mean(resultados[q]):.2f}")
