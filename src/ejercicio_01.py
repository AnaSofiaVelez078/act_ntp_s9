from dataframe import get_dataframe

df = get_dataframe()

# Empleados con salario mayor a 50,000
print("\nEmpleados con salario > 50,000:")
print(df[df['salario'] > 50000])

# Empleados menores de 35 años
print("\nEmpleados con edad < 35:")
print(df[df['edad'] < 35])

# Empleados del departamento 'IT'
print("\nEmpleados del departamento IT:")
print(df[df['departamento'] == 'IT'])