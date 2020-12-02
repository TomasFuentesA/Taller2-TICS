import random
random.seed()

def Generar_mediciones(registro):
    ide=0
    luz=0
    hum=0
    temp=0
    idmed=0
    hora=800
    minus=800
    while(ide<100):   
        luz=random.randrange(0,50)
        hum=random.randrange(0,100)
        temp=random.randrange(5,40)
        if(luz in range (10,30) and hum in range (10,30) and  temp in range (10,30)):
            a=[str(ide),str(luz),str(hum),str(temp),str(hora),str(idmed)]
            idmed+=1
        else:
            a=[str(ide),str(luz),str(hum),str(temp),str(hora)]
        if (hora-minus==60):
            hora+=40
            minus+=100
        else:
            hora+=10
            if (hora-minus==60):
                hora+=40
                minus+=100
        ide=ide+1
        registro.append(a)

    return registro

def Generar_riego(mediciones,riegos):
    for i in mediciones:
        if (len(i)==6):
            ide = i[5]
            time=random.randrange(8,20)
            a=[str(ide),str(time)]
            riegos.append(a)
        else:
            continue
    return riegos


def Generar_sensores(sensores):
    ides=[0,0,0,0,1,1,1,1,2,2,2,2]
    ide=0
    for i in ides:
        state=random.randrange(0,5)
        if (i==0):
            tipo='luz'
        if (i==1):
            tipo='humedad'
        if (i==2):
            tipo='temperatura'
        a=[str(ide),str(state),tipo]
        sensores.append(a)
        ide+=1
    return sensores


def Unir_tablas(sensores,mediciones,union):
    for i in mediciones:
        ide_med=i[0]
        for j in sensores:
            ide_sen=j[0]
            a=[str(ide_med),str(ide_sen)]
            union.append(a)
    return union


def escribir(lista,nombre):
    f=open(nombre,'w')
    for i in lista:
        linea=(',').join(i)
        linea=linea+'\n'
        f.write(linea)
    return

if __name__ == "__main__":
    tabla_mediciones=[]
    riegos=[]
    sensores=[]
    union=[]
    Generar_mediciones(tabla_mediciones)
    Generar_riego(tabla_mediciones,riegos)
    Generar_sensores(sensores)
    Unir_tablas(sensores,tabla_mediciones,union)
    print('------------------ mediciones -------------------')
    print(tabla_mediciones)
    print('------------------ riegos -------------------------')
    print(riegos)
    print('------------------ sensores -------------------------')
    print(sensores)
    print('------------------ sensor_medicion -------------------------')
    print(union)
    escribir(riegos,'Riegos')
    escribir(sensores,'Sensores')
    escribir(union,'Sensor_Medi')
    escribir(tabla_mediciones,'Mediciones')
    


    