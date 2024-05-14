
import pulp as lp

#variables de decisión
wv = lp.LpVariable("wv", lowBound=0, cat='Continuous')
wf = lp.LpVariable("wf", lowBound=0, cat='Continuous')
wc = lp.LpVariable("wc", lowBound=0, cat='Continuous')
wu = lp.LpVariable("wu", upBound=0, cat='Continuous')
ws = lp.LpVariable("ws", upBound=0, cat='Continuous')
wch = lp.LpVariable("wch", upBound=0, cat='Continuous')
wt = lp.LpVariable("wt", upBound=0, cat='Continuous')

# Crear un problema de programación lineal
prob = lp.LpProblem("ProblemaDual", lp.LpMaximize)
#función objetivo
prob += 70*wv + 45*wf + 55*wc + 45*wu + 40*ws + 45*wch + 40*wt

#restricciones
prob += wv + wu <= 30000
prob += wv + ws <= 31000
prob += wv + wch <= 32000
prob += wv + wt <= 29000
prob += wf + wu <= 29000
prob += wf + ws <= 28000
prob += wf + wch <= 30000
prob += wf + wt <= 28000
prob += wc + wu <= 33000
prob += wc + ws <= 32000
prob += wc + wch <= 34000
prob += wc + wt <= 31000

#resolver el problema
prob.solve(lp.PULP_CBC_CMD(msg=0))
print("Status:", lp.LpStatus[prob.status])
print("Función objetivo = ", lp.value(prob.objective))
for v in prob.variables():
    print(v.name, "=", v.varValue)

