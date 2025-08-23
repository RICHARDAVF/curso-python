class Vehiculo:
    def __init__(self,marca:str,modelo:str,year:int):
        self.marca = marca
        self.modelo = modelo
        self.year = year
    def mostrar_info(self)->str:
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.year}"
    def __str__(self)->str:
        return f"{self.marca}-{self.modelo}-{self.year}"

class Coche(Vehiculo):
    def __init__(self,marca:str,modelo:str,year:int,numero_puertas:int):
        super().__init__(marca,modelo,year)
        self.numero_puertas = numero_puertas
    def mostrar_info(self):
        return f"Marca:{self.marca}. Modelo: {self.modelo},Año:{self.year}, # de puertas: {self.numero_puertas}"
    
    
class Motocicleta(Vehiculo):
    def __init__(self,marca:str,modelo:str,year:int,tipo_motor:str):
        super().__init__(marca,modelo,year)
        self.tipo_motor = tipo_motor
    def mostrar_info(self):
        return f"Marca:{self.marca}. Modelo: {self.modelo},Año:{self.year}, Tipo de motor: {self.tipo_motor}"
coche = Coche("Toyota","Corolla",2022,4)
moto = Motocicleta("Honda","CBR500",2023,"Gasolina")
print(coche.mostrar_info())
print(moto.mostrar_info())
