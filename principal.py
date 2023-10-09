from inmobiliaria import Inmobiliaria
from departamento import Departamento
from casa import Casa


def cargarArchivo(archivo, inmobiliaria:Inmobiliaria):
    arc = open(archivo, "r")
    for linea in arc.readlines():
        lista = linea.strip().split(",")
        if int(lista[0]) == 1:
            inmobiliaria.cargarInmueble(Casa(int(lista[1]), lista[2], int(lista[4]), float(lista[3]), int(lista[5]), (True if int(lista[6]) == 1 else False)))
        else:
            inmobiliaria.cargarInmueble(Departamento(int(lista[1]), lista[2], int(lista[4]), float(lista[3]), float(lista[5]), int(lista[6])))
    arc.close()


def main():
    # Inicializo Inmobiliaria
    inm = Inmobiliaria("Inmobiliaria Rez")
    # Carga de archivos
    cargarArchivo("inmuebles.csv", inm)
    
    #prueba de errores...
    #inm.vaciarInmuebles()
    print("-----------------------------------")
    # Suma de alquileres total
    try:
        sumaAlquileres = inm.sumaAlquileres()
    except TypeError as e:
        print(f"Error de tipos {e}")
    except Exception as e:
        print(f"Se ha producido un error {e}")
    else:
        print(f"El total de dinero a recaudar si todos los inmuebles son alquilados es de: {sumaAlquileres}")
        
    print("-----------------------------------")
    # Cantidad de casas premium
    try:
        casasPremium = inm.cantidadCasasPremium()
    except TypeError as e:
        print(f"Error de tipos {e}")
    except Exception as e:
        print(f"Se ha producido un error {e}")
    else:
            print(f"Hay un total de {casasPremium} Casas premium")
            
    print("-----------------------------------")   
    # Propietario cuyo alquiler es el mas bajo
    try:
        propietario = inm.propietarioDelAlquilerMasBajo()
    except TypeError as e:
        print(f"Error de tipos {e}")
    except Exception as e:
        print(f"Se ha producido un error {e}")
    else:
        print(f"El propietario cuyo alquiler definitivo es mas bajo es: {propietario}")

    
    print("------------")
    #pruebas
    """
    for i in inm.inmuebles.values():
        print(i)
    """
    # cantidad de inmuebles
    #print(len(inm.inmuebles.values()))
if __name__ == "__main__":
    main()