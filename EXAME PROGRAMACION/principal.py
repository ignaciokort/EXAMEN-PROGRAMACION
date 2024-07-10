import funciones as fn

trabajadores = [
    'Juan Pérez','María García','Carlos López','Ana Martínez','Pedro Rodríguez','Laura Hernández','Miguel Sánchez',
    'Isabel Gómez','Francisco Díaz','Elena Fernández'
]
registro_sueldo={}
while True:
    print("=====MENU=====")
    print("0. Inicializar sueldos de empleados")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadisticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    opcion =int(input("Seleccione: "))
    if opcion == 0:
        registro_sueldo = {trabajador : 0 for trabajador in trabajadores}
    elif opcion ==1:   
        if registro_sueldo:          
            registro_sueldo = fn.Generar_sueldos(trabajadores)
        else:
            print("porfavor debe inicializar primero con el numero 0.")
    elif opcion ==2:
        if registro_sueldo:
            fn.Clasificar_sueldos(registro_sueldo)
        else:
            print("debe generar sueldo aleatorio primero.")
    elif opcion ==3:
        sueldo_mas_alto,sueldo_mas_bajo,prom_sueldo=fn.Ver_estadisticas(registro_sueldo)
        print("EL SUELDO MAS ALTO ES : ",sueldo_mas_alto)
        print("El SUELDO MAS BAJO ES :",sueldo_mas_bajo)
        print("EL PROMEDIO DE SUELDO ES:",prom_sueldo)
    elif opcion ==4:
        fn.Reporte_sueldos(registro_sueldo)
    elif opcion ==5:
        print("Finalizando programa....")
        print("desarrollado por Ignacio Kort")
        print("RUT 21.049.628-9")
        break

