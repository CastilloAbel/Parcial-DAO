class Inmueble:
        def __init__(self, codigo:int, nombre_propietario:str, superficie:int, importe_base_alquiler_mensual:float) -> None:
            self._codigo = codigo
            self._nombre_propietario = nombre_propietario
            self._superficie = superficie
            self._importe_base_alquiler_mensual = importe_base_alquiler_mensual
        
        @property
        def codigo(self):
            return self._codigo
         
        @property
        def nombre_propietario(self):
            return self._nombre_propietario
        
        @property
        def superficie(self):
            return self._superficie
        
        @property
        def importe_base_alquiler_mensual(self):
            return self._importe_base_alquiler_mensual
        
        def importeDefinitivo(self)->float:
            return self.importe_base_alquiler_mensual
        
        def __str__(self) -> str:
            return f"Codigo: {self.codigo}, Propietario: {self.nombre_propietario}, Superficie: {self.superficie}, ImporteBase: {self.importe_base_alquiler_mensual}$"
        