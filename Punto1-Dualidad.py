
import pulp as plp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------
# Creación del objeto problema en PuLP
# -----------------
prob= plp.LpProblem("Dualidad",plp.LpMinimize)

# -----------------------------
# Variables de Decisión
# -----------------------------
w= {i:plp.LpVariable(f"w_{i}",lowBound=0,upBound=None,cat=plp.LpContinuous) for i in range(1,6)}

# -----------------------------
# Función Objetivo
# -----------------------------
prob += 105*w[1] + 765*w[2] + 220*w[3] - 120*w[4] + 225*w[5]

# -----------------------------
# Restricciones
# -----------------------------
prob += 7*w[1] + w[3] - w[4] >= 17
prob += 2*w[2] + w[3] >= 30
prob += 15*w[1] + 5*w[2] - 2*w[4] >= -4
prob += 3*w[2] + 3*w[5] >= 5
prob += -w[4] + w[5] >= -10

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
    print(f"w_{i} = {round(plp.value(w[i]),2)}")




