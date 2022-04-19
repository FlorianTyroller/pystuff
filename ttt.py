import numpy as np
from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('GLOP')

x = solver.NumVar(0, solver.infinity(), 'x')
y = solver.NumVar(0, solver.infinity(), 'y')

solver.Add(x + 2*y <= 14)
solver.Add(3*x - y >= 0)
solver.Add(x - y <= 2)

solver.Maximize(3*x + 3*y)

status = solver.Solve()

print(x.solution_value(),y.solution_value())