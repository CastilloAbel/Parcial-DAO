from inmueble import Inmueble
class Casa(Inmueble):
    def __init__(self, codigo:int, nombre_propietario:str, superficie:int, importe_base_alquiler_mensual:float, cant_dormitorio:int, tiene_pileta:bool) -> None:
        super().__init__(codigo, nombre_propietario, superficie, importe_base_alquiler_mensual)
        self._cant_dormitorio = cant_dormitorio
        self._tiene_pileta = tiene_pileta
        
    @property
    def cant_dormitorio(self):
        return self._cant_dormitorio
    
    @property
    def tiene_pileta(self):
        return self._tiene_pileta
    
    def importeDefinitivo(self):
        return super().importeDefinitivo() + (self.cant_dormitorio * 30000) + (100000 if self.tiene_pileta else 0)
    
    def __str__(self) -> str:
        return super().__str__() + f", Cantidad de dormitorios: {self.cant_dormitorio}, Pileta: {'Si' if self.tiene_pileta else 'No'}, ImporteDefinitivo: {self.importeDefinitivo()}$"
    
    