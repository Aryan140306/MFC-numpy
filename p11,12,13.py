import sympy as sp

# Define variables
x, y, z = sp.symbols('x y z')

# Input scalar function for gradient
scalar_field = input("Enter scalar function f(x,y,z): ")
f = sp.sympify(scalar_field)

# Compute gradient (∇f)
gradient_f = sp.Matrix([f.diff(var) for var in (x, y, z)])
print("Gradient of the scalar field:")
sp.pprint(gradient_f)

# Input vector field components for divergence and curl
print("\nEnter vector field components P, Q, R as functions of x, y, z:")
P = sp.sympify(input("P = "))
Q = sp.sympify(input("Q = "))
R = sp.sympify(input("R = "))

# Vector field
F = sp.Matrix([P, Q, R])

# Compute divergence (∇·F)
divergence_F = sp.diff(P, x) + sp.diff(Q, y) + sp.diff(R, z)
print("\nDivergence of the vector field:")
sp.pprint(divergence_F)

# Compute curl (∇×F)
curl_F = sp.Matrix([
    sp.diff(R, y) - sp.diff(Q, z),
    sp.diff(P, z) - sp.diff(R, x),
    sp.diff(Q, x) - sp.diff(P, y)
])
print("\nCurl of the vector field:")
sp.pprint(curl_F)
