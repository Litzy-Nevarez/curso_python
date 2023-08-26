staff = {
    'Juan': {
        'cargo': 'marketing',
        'desempeño': 71
    },
    'Sofia': {
        'cargo': 'marketing',
        'desempeño': 65
    },
    'Andres': {
        'cargo': 'marketing',
        'desempeño': 49
    },
    'Romina': {
        'cargo': 'marketing',
        'desempeño': 53
    }
}

def identificar_y_despedir_bajo_desempenio(staff_dict):
    empleados_a_despedir = []

    for empleado, detalles in staff_dict.items():
        desempenio = detalles['desempeño']
        if desempenio < 50:
            print("Se recomienda despedir al trabajador {empleado}")
            empleados_a_despedir.append(empleado)
    

    for empleado_a_despedir in empleados_a_despedir:
        del staff_dict[empleado_a_despedir]

identificar_y_despedir_bajo_desempenio(staff)
print("Los trabajadores con mejor desempeño: ")


