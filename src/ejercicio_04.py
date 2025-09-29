from dataframe import get_dataframe

df = get_dataframe()

# Empleados cuyos nombres empiezan con 'M'
print("\nEmpleados cuyos nombres empiezan con 'M':")
print(df[df['nombre'].str.startswith('M')])

# Departamentos que contienen 'R'
print("\nDepartamentos que contienen 'R':")
print(df[df['departamento'].str.contains('R')])