import pulp as lp
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def evaluate_model(b):
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

        # -----------------
        # Función objetivo
        # -----------------
        prob+= 12000*x_coco + 9500*x_almendra

        # -----------------
        # Restricciones
        # -----------------
        # No excederse en la cantidad de tiempo de producción
        prob+= 3.4*x_coco + 2.6*x_almendra <= 720

        # No pasarse de la cantidad de coco disponible
        prob+= 0.35*x_coco <= 17.8

        # No pasarse de la cantidad de almendra disponible
        prob+= 0.37*x_almendra <= 15.2

        # No pasarse de los litros de agua disponibles
        prob+= 0.4*x_coco + 0.47*x_almendra <= 42

        # No pasarse de la capacidad de producción
        prob+= 0.75*x_coco + 0.84*x_almendra <= b

        # ---------------------
        # Solución del problema
        # ---------------------
        prob.solve(lp.PULP_CBC_CMD(msg=0))

        return prob.objective.value()


# -------------------------------------
# Valores de b a evaluar
# -------------------------------------
values = [i for i in range(0,90)]

# -------------------------------------
# Crear lista vacía para almacenar el valor de la variable primal
# -------------------------------------
primales = []
df = pd.DataFrame()

# -------------------------------------
# Proceso iterativo
# -------------------------------------
for b in values:
    valor = round(evaluate_model(b),0)
    primales.append(valor)
    df = df._append({"Capacidad de producción de VeggieDrinks": b, "Función Objetivo (Utilidad total)": valor}, ignore_index=True)

# -------------------------------------
# Graficar el los resultados
# -------------------------------------
plt.scatter(values, primales, color = "pink")
plt.xlabel("Capacidad de producción de VeggieDrinks")
plt.ylabel("Función Objetivo (Utilidad total)")
plt.title("Valor de la variable primal por cada litro de capacidad de producción de VeggieDrinks")

plt.show()


# Guardar los resultados en un archivo excel
df.to_excel("Resultados_punto3.xlsx", index = False)


