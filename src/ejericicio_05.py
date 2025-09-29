from dataframe import get_dataframe

df = get_dataframe()

# Empleados de IT con más de 30 años Y salario mayor a 60,000
print("\nEmpleados de IT con más de 30 años y salario > 60,000:")
print(df[(df['departamento'] == 'IT') & (df['edad'] > 30) & (df['salario'] > 60000)])

# Empleados cuyo nombre empieza con 'L' O son de RRHH
print("\nEmpleados cuyo nombre empieza con 'L' O son de RRHH:")
print(df[(df['nombre'].str.startswith('L')) | (df['departamento'] == 'RRHH')])