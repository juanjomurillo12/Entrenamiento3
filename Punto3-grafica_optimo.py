import pulp as lp
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



# Valor del lado derecho de la restricción R5

b=0

# lista donde se guardarán los resultados de cada iteración

resultados = []

# valor de la variable dual

dual = 1

# Ciclo while que corre el modelo iterativamente

while dual > 0:

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
        prob+= 3.4*x_coco + 2.6*x_almendra <= 720, "R1"

        # No pasarse de la cantidad de coco disponible
        prob+= 0.35*x_coco <= 17.8, "R2"

        # No pasarse de la cantidad de almendra disponible
        prob+= 0.37*x_almendra <= 15.2, "R3"

        # No pasarse de los litros de agua disponibles
        prob+= 0.4*x_coco + 0.47*x_almendra <= 42, "R4"

        # No pasarse de la capacidad de producción
        prob+= x_coco + x_almendra <= b, "R5"

        # Resolver el problema
        prob.solve(lp.PULP_CBC_CMD(msg=0))

        # Guardar el valor de la función objetivo
        f_o = lp.value(prob.objective)

        # Guardar el valor de la variable dual
        dual = prob.constraints["R5"].pi

        # diccionario con los resultados de la iteración
        resultado = {
            "Recurso": b,
            "F.O": f_o,
            "Dual": dual,
            "Estado": lp.LpStatus[prob.status]}
        
        # Guardar el resultado en la lista de resultados
        resultados.append(resultado)

        # Aumentar el valor de b en 0.1
        b += 0.1


    

    

# Dar formato de tabla a los resultados con la librería "Pandas"
# Guardar la tabla en el objeto "df"
df = pd.DataFrame(resultados)
# Visualizar cómo luce la tabla
print(df)


#*-------*-------*
#Imprimir Gráfica
#*-------*-------*

#Crear gráfica y sub-gráfica que sobrelapa a la primera y aporta los
#títulos a los ejes
fig, gra = plt.subplots()

#Indicamos qué info va en el eje "x" y en el "y"
gra.plot(df['Recurso'],df['F.O'], color='pink')

#Dar formato a la gráfica
gra.set(xlabel='Recurso',ylabel='Valor F.O',title='F.O vs Capacidad de Producción')
plt.grid()

#Mostrar gráfica
plt.show()

# %%

