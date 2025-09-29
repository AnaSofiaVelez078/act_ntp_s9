import pandas as pd

def get_dataframe():
    data = {
        'nombre': ['Ana', 'Luis', 'Carmen', 'José', 'María', 'Pedro', 'Laura', 'Miguel'],
        'departamento': ['Ventas', 'IT', 'RRHH', 'Ventas', 'IT', 'Marketing', 'RRHH', 'IT'],
        'salario': [45000, 65000, 50000, 48000, 70000, 55000, 52000, 68000],
        'edad': [28, 35, 42, 31, 29, 38, 45, 33]
    }

    return pd.DataFrame(data)