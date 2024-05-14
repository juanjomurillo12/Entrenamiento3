import pulp as lp
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd


# Guardar nombre del archivo en una variable
file_name = 'Excel-Punto2_Carga_De_datos.xlsx'

# -----------------
# Conjuntos
# -----------------

conjuntos = pd.read_excel(io=file_name, sheet_name ="Conjuntos")

# Conjunto de helados
H = [i for i in conjuntos["Sabores"] if not pd.isna(i)]

# Conjunto de sucursales
S = [i for i in conjuntos["Sucursales"] if not pd.isna(i)]

# -----------------
# Parámetros
# -----------------

req_min = pd.read_excel(file_name, sheet_name = 'Requerimiento Minimo', index_col=0).squeeze()

# Requerimiento mínimo de helado j
r = {j:req_min[j] for j in H}

req_max = pd.read_excel(file_name, sheet_name = 'Cantidad Maxima Mensual', index_col=0).squeeze()

# Requerimiento máximo de helado en la sucursal i
m = {i:req_max[i] for i in S}

costos = pd.read_excel(file_name, sheet_name = 'Costos', index_col=(0,1)).squeeze()

# Costo de comprar helado j a la sucursal i
c = {(i,j):costos[i][j] for i in S for j in H}

# ---------------------
# Creación del objeto problema en PuLP
# ---------------------
prob= lp.LpProblem("Distribucion_de_helados",sense = lp.LpMaximize)

# -----------------------------
# Variables de Decisión
# -----------------------------
# Variable que indica el cambio en los costos si aumenta el requerimiento mínimo de helado j en un litro
w = {j:lp.LpVariable(f'cambio_{j}',lowBound=0, cat=lp.LpContinuous)for j in H}

# variable que indica en cambio en los costos si aumenta la cantidad de helado en la sucursal i en un litro
z = {i:lp.LpVariable(f'cambio_{i}',upBound=0, cat=lp.LpContinuous)for i in S}

# -----------------------------
# Función objetivo
# -----------------------------
prob+= lp.lpSum(w[j]*r[j] for j in H) + lp.lpSum(z[i]*m[i] for i in S)

# -----------------------------
# Restricciones
# -----------------------------
# Restricciones asociadas a la cantidad de helado que se compra a cada sucursal
for i in S:
    for j in H:
        prob+= w[j] + z[i] <= c[i,j]


# -----------------------------
# Solución del problema
# -----------------------------
prob.solve(lp.PULP_CBC_CMD(msg=0))
# -----------------------------
# Impresión de resultados
# -----------------------------
print("Estado:", lp.LpStatus[prob.status])
print("Costo total:", lp.value(prob.objective))
print("Cambio en los costos si aumenta el requerimiento mínimo de helado en un litro")
for j in H:
    print(f"Helado {j}: {w[j].varValue}")
print("Cambio en los costos si aumenta la cantidad de helado en la sucursal en un litro")
for i in S:
    print(f"Sucursal {i}: {z[i].varValue}")



