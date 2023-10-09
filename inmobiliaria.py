from inmueble import Inmueble
from casa import Casa
from functools import reduce
class Inmobiliaria:
    def __init__(self, nombre) -> None:
        self._nombre = nombre
        self._inmuebles = dict()
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def inmuebles(self):
        return self._inmuebles
    
    @inmuebles.setter
    def inmuebles(self, inmueble):
        self._inmuebles = inmueble
        
    def cargarInmueble(self, inmueble:Inmueble):
        self.inmuebles[inmueble.codigo] = inmueble
    
    def vaciarInmuebles(self):
        self.inmuebles.clear()
        
    def __str__(self) -> str:
        return f"Nombre del inmueble: {self.nombre}"
    
    def sumaAlquileres(self)->float:
        return sum(list(map(lambda x: x.importeDefinitivo(), self.inmuebles.values())))
    
    def cantidadCasasPremium(self)->int:
        return len(list(filter(lambda x: isinstance(x, Casa) and x.superficie > 150 and x.cant_dormitorio > 2 and x.tiene_pileta, self.inmuebles.values())))
    
    def propietarioDelAlquilerMasBajo(self)->str:
        return reduce(lambda x, y: x if x.importeDefinitivo() < y.importeDefinitivo() else y, self.inmuebles.values()).nombre_propietario