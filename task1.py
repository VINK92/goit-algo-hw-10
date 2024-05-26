import pulp

model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

x = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
y = pulp.LpVariable('FruitJuice', lowBound=0, cat='Continuous')

model += x + y, "Total_Production"

model += 2*x + y <= 100, "Water_Limit"
model += x <= 50, "Sugar_Limit"
model += x <= 30, "LemonJuice_Limit"
model += 2*y <= 40, "FruitPuree_Limit"

model.solve()

print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Optimal number of Lemonades to produce: {pulp.value(x)}")
print(f"Optimal number of Fruit Juices to produce: {pulp.value(y)}")
print(f"Maximum total production: {pulp.value(model.objective)}")
