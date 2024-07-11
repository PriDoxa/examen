import funciones as fn

estadisticas={}

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
sueldos_trabajadores= {trabajadores:0 for trabajador in trabajadores}

while True:
    try:
        print("---menu---")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadisticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")

        opcion=int(input("ingrese su opcion"))

        if opcion==1:
            sueldos_trabajadores=fn.asignar_sueldos_aleatorios(trabajadores)

        elif opcion ==2:
            fn.clasificar_sueldos(sueldos_trabajadores)



        elif opcion ==3:
            fn.ver_estadistica(trabajadores)
            print("sueldo mas alto"), estadisticas
            print("suledo mas bajo"), estadisticas
            print("promedio de sueldo"), estadisticas

        elif opcion ==4:
            fn.reporte_sueldo(trabajadores)
            

        elif opcion==5:
            break    
















