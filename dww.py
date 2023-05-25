from sympy import symbols, Eq, solve

P = symbols('P')
Qd = 30 - 3.5 * P
Qs = 5 + 1.5 * P

equation1 = Eq(Qd, Qs)
solution = solve(equation1, P)

price_equilibrium = solution[0]
quantity_equilibrium = Qd.subs(P, price_equilibrium)

print("El precio de equilibrio es:", price_equilibrium)
print("La cantidad de equilibrio es:", quantity_equilibrium)
