from dataframe import get_dataframe

df = get_dataframe()

# Empleados de IT Y salario mayor a 60,000
print("\nEmpleados de IT con salario > 60,000:")
print(df[(df['departamento'] == 'IT') & (df['salario'] > 60000)])

# Empleados de Ventas O mayores de 40 años
print("\nEmpleados de Ventas O mayores de 40 años:")
print(df[(df['departamento'] == 'Ventas') | (df['edad'] > 40)])

# Empleados que NO son de Marketing
print("\nEmpleados que NO son de Marketing:")
print(df[~(df['departamento'] == 'Marketing')])