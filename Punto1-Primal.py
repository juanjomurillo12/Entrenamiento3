
import pulp as plp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------
# Creación del objeto problema en PuLP
# -----------------
prob= plp.LpProblem("Dualidad",plp.LpMaximize)

# -----------------------------
# Variables de Decisión
# -----------------------------
x= {i:plp.LpVariable(f"x_{i}",lowBound=0,upBound=None,cat=plp.LpContinuous) for i in range(1,6)}
s= {i:plp.LpVariable(f"s_{i}",lowBound=0,upBound=None,cat=plp.LpContinuous) for i in range(1,6)}
# -----------------------------
# Función Objetivo
# -----------------------------
prob += 17*x[1] + 30*x[2] - 4*x[3] + 5*x[4] - 10*x[5] + 0*s[1] + 0*s[2] + 0*s[3] + 0*s[4] + 0*s[5]

# -----------------------------
# Restricciones
# -----------------------------
prob += 7*x[1] + 15*x[3] + s[1] == 105
prob += 2*x[2] + 5*x[3] + 3*x[4] + s[2] == 765
prob += x[1] + x[2] + s[3] == 220
prob += -x[1] - 2*x[3] - x[5] + s[4] == -120
prob += 3*x[4] + x[5] + s[5] == 225

# -----------------------------
# Resolver el problema
# -----------------------------
prob.solve(plp.PULP_CBC_CMD(msg=0))

# -----------------------------
# Impresión de resultados
# -----------------------------
print("Estado:", plp.LpStatus[prob.status])
print("El valor de la F.O. es:", round(plp.value(prob.objective),2))
for i in range(1,6):
    print(f"x_{i} = {round(plp.value(x[i]),2)}")
    print(f"s_{i} = {round(plp.value(s[i]),2)}")




