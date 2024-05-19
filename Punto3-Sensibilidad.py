import pulp as lp
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd

# ---------------------
# Creación del objeto problema en PuLP
# ---------------------
prob= lp.LpProblem("Veggie_Drinks",sense = lp.LpMaximize)

# -----------------
# Variables de Decisión
# -----------------
# Litros de bebida de coco
x_coco = lp.LpVariable('x_coco',lowBound=0, cat=lp.LpContinuous)

# Litros de bebida de almendra
x_almendra = lp.LpVariable('x_almendra',lowBound=0, cat=lp.LpContinuous)

# Variables de holgura para las restricciones
x1 = lp.LpVariable('x1',lowBound=0, cat=lp.LpContinuous)
x2 = lp.LpVariable('x2',lowBound=0, cat=lp.LpContinuous)
x3 = lp.LpVariable('x3',lowBound=0, cat=lp.LpContinuous)
x4 = lp.LpVariable('x4',lowBound=0, cat=lp.LpContinuous)
x5 = lp.LpVariable('x5',lowBound=0, cat=lp.LpContinuous)

# -----------------
# Función objetivo
# -----------------
prob+= 12000*x_coco + 9500*x_almendra

# -----------------
# Restricciones
# -----------------
# No excederse en la cantidad de tiempo de producción
prob+= 3.4*x_coco + 2.6*x_almendra + x1 == 720

# No pasarse de la cantidad de coco disponible
prob+= 0.35*x_coco +x2 == 17.8

# No pasarse de la cantidad de almendra disponible
prob+= 0.37*x_almendra +x3 ==  15.2

# No pasarse de los litros de agua disponibles
prob+= 0.4*x_coco + 0.47*x_almendra + x4 == 42

# No pasarse de la capacidad de producción
prob+= x_coco + x_almendra + x5 == 75

# ---------------------
# Solución del problema
# ---------------------
prob.solve(lp.PULP_CBC_CMD(msg=0))

# ---------------------
# Resultados
# ---------------------
print(f'Status: {lp.LpStatus[prob.status]}')
print(f'Utilidad total: {round(lp.value(prob.objective),2)}')
print(f'Litros de bebida de coco: {round(x_coco.varValue,2)}')
print(f'Litros de bebida de almendra: {round(x_almendra.varValue,2)}')
print(f'Holgura x1: {round(x1.varValue,2)}')
print(f'Holgura x2: {round(x2.varValue,2)}')
print(f'Holgura x3: {round(x3.varValue,2)}')
print(f'Holgura x4: {round(x4.varValue,2)}')
print(f'Holgura x5: {round(x5.varValue,2)}')


