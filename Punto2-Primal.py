
import pulp as lp

#variables de decisión
xvu = lp.LpVariable("xvu", 0, None, lp.LpContinuous)
xvs = lp.LpVariable("xvs", 0, None, lp.LpContinuous)
xvc = lp.LpVariable("xvc", 0, None, lp.LpContinuous)
xvt = lp.LpVariable("xvt", 0, None, lp.LpContinuous)
xfu = lp.LpVariable("xfu", 0, None, lp.LpContinuous)
xfs = lp.LpVariable("xfs", 0, None, lp.LpContinuous)
xfc = lp.LpVariable("xfc", 0, None, lp.LpContinuous)
xft = lp.LpVariable("xft", 0, None, lp.LpContinuous)
xcu = lp.LpVariable("xcu", 0, None, lp.LpContinuous)
xcs = lp.LpVariable("xcs", 0, None, lp.LpContinuous)
xcc = lp.LpVariable("xcc", 0, None, lp.LpContinuous)
xct = lp.LpVariable("xct", 0, None, lp.LpContinuous)

#creacion del problema
prob = lp.LpProblem("Problema", lp.LpMinimize)
#función objetivo
prob += 30000*xvu + 31000*xvs + 32000*xvc + 29000*xvt + 29000*xfu + 28000*xfs + 30000*xfc + 28000*xft + 33000*xcu + 32000*xcs + 34000*xcc + 31000*xct

#restricciones
prob += xvu + xvs + xvc + xvt >= 70
prob += xfu + xfs + xfc + xft >= 45
prob += xcu + xcs + xcc + xct >= 55
prob += xvu + xfu + xcu <= 45
prob += xvs + xfs + xcs <= 40
prob += xvc + xfc + xcc <= 45
prob += xvt + xft + xct <= 40

#solución
prob.solve(lp.PULP_CBC_CMD(msg=0))
print("Status:", lp.LpStatus[prob.status])
print("Función objetivo = ", lp.value(prob.objective))
for v in prob.variables():
    print(v.name, "=", v.varValue)
