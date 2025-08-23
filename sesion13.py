# Uso de __main__ y __name__
def contar_palabras(texto):
    return len(texto.split())
def invetir_texto(texto):
    return texto[::-1]
def en_mayuscula(texto):
    return texto.upper()

if __name__ == "__main__":
    print("-- Demostracion --")
    texto = "Hola mundo, esto es una prueba de python"
    print(texto)
    palabras = contar_palabras(texto)
    print(f"la cantidad de palabras es: {palabras}")