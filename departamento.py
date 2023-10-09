from inmueble import Inmueble

class Departamento(Inmueble):
    def __init__(self, codigo:int, nombre_propietario:str, superficie:int, importe_base_alquiler_mensual:float, importe_expensas:float, nro_piso:int) -> None:
        super().__init__(codigo, nombre_propietario, superficie, importe_base_alquiler_mensual)
        self._importe_expensas = importe_expensas
        self._nro_piso = nro_piso
        
    @property
    def importe_expensas(self):
        return self._importe_expensas
    
    @property
    def nro_piso(self):
        return self._nro_piso
        
    def importeDefinitivo(self):
        return super().importeDefinitivo() + (20000 if self.nro_piso < 3 else 0) + self.importe_expensas
    
    def __str__(self) -> str:
        return super().__str__() + f", Importe Expensas: {self.importe_expensas}$, Nro de piso: {self.nro_piso}, ImporteDefinitivo: {self.importeDefinitivo()}$"
    