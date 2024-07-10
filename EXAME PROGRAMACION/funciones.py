import random
import csv
import statistics
def Generar_sueldos(trabajadores):
    registro_sueldo={}
    for trabajador in trabajadores:
        sueldo = random.randint(300000,2500000)
        registro_sueldo[trabajador]=sueldo
    print("Sueldo creados Aleatoriamente")
    print(registro_sueldo)
    return registro_sueldo

def Clasificar_sueldos(registro_sueldo):
    #200 = $2.000.000
    menor_800={}
    entre_800_200 = {}
    mayor_200 ={}
    for trabajador, sueldo in registro_sueldo.items():
        if sueldo < 800000:
            menor_800[trabajador] = sueldo 
        elif sueldo <=2000000:
            entre_800_200[trabajador]=sueldo
        else:
            mayor_200[trabajador]=sueldo
    print("Sueldos menores a $800.000 TOTAL: ",len(menor_800))
    for trabajador,sueldo in menor_800.items():
        print(trabajador,": ",sueldo)
    print("Sueldos entre $800.000 y $2.000.000: ",len(entre_800_200))
    for trabajador,sueldo in entre_800_200.items():
        print(trabajador,": ",sueldo)
    print("Sueldos mayores a 2.000.000: ",len(mayor_200))
    for trabajador,sueldo in mayor_200.items():
        print(trabajador,": ",sueldo)       



def Ver_estadisticas(registro_sueldo):
    sueldo = list(registro_sueldo.values())

    sueldo_mas_alto = max(sueldo)
    sueldo_mas_bajo = min(sueldo)
    prom_sueldo = sum(sueldo)/len(sueldo)
    #media_geometrica = statistics(sueldo_mas_alto,sueldo_mas_bajo,prom_sueldo) no se como se utiliza 
    return sueldo_mas_alto,sueldo_mas_bajo,prom_sueldo#media_geometrica

def Reporte_sueldos(registro_sueldo):
    
    with open('reporte_sueldo.csv','w',newline='') as archivo:
        escritor =csv.writer(archivo,delimiter=',')
        escritor.writerow(['NOMBRES_TRABAJADORES','SUELDO BASE','DESCUENTO,SALUD, DESCUENTO AFP,SUELDO LIQUIDO'])
        for trabajador,sueldo in registro_sueldo.items():
            escritor.writerow([trabajador,": ",sueldo])
        print("reporte excel generado con exito.")
        print("esta en la carpeta para q lo abra")

