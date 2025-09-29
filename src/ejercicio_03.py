from dataframe import get_dataframe

df = get_dataframe()

# Empleados de IT o Ventas
print("\nEmpleados de IT o Ventas:")
print(df[df['departamento'].isin(['IT', 'Ventas'])])

# Empleados con edad de 28, 35 o 42 años
print("\nEmpleados con edad 28, 35 o 42:")
print(df[df['edad'].isin([28, 35, 42])])