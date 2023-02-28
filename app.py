operaciones_mes = [-100000, 60000, 200000, 150000, -220000, -112000]

def analisis(operaciones): 
    acumulador_gastos = 0
    acumulador_ingresos = 0

    for operacion in operaciones:
        if operacion<0:
            print(operacion, "es un gasto")
            acumulador_gastos += operacion
        else: 
            print(operacion, "es un ingreso")
            acumulador_ingresos += operacion
    print("se gasto ", acumulador_gastos, "se ingrese ", acumulador_ingresos) 
    print("el balance es ", acumulador_ingresos + acumulador_gastos)       

analisis(operaciones_mes)



