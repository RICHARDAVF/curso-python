import multiprocessing
import time

def calculadora_worker(cola_de_tareas, cola_de_resultados):
    """
    Proceso trabajador que toma una tarea de la cola, la ejecuta y
    pone el resultado en la cola de resultados.
    """
    print(f"[{multiprocessing.current_process().name}] Iniciado y listo para calcular.")
    while True:
        # Espera y obtiene una tarea. Bloquea hasta que haya un item.
        tarea = cola_de_tareas.get()

        # Señal de parada: si la tarea es None, termina el bucle.
        if tarea is None:
            print(f"[{multiprocessing.current_process().name}] Recibió señal de parada. Terminando.")
            break

        num1, operador, num2 = tarea
        resultado = None

        # Simula un cálculo que toma tiempo
        time.sleep(0.5)

        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Error: División por cero"
        else:
            resultado = f"Error: Operador '{operador}' no válido"

        # Pone el resultado en la cola de resultados
        cola_de_resultados.put(f"{num1} {operador} {num2} = {resultado}")

if __name__ == "__main__":
    print("[Proceso Principal] Iniciando Calculadora Distribuida...")

    # 1. Crear colas para comunicar tareas y resultados
    cola_de_tareas = multiprocessing.Queue()
    cola_de_resultados = multiprocessing.Queue()

    # 2. Definir las operaciones a realizar
    operaciones = [
        (5, '+', 3), (10, '*', 2), (20, '-', 5), (15, '/', 3),
        (100, '/', 0), (7, '**', 2), (88, '+', 12), (50, '*', 3)
    ]
    num_tareas = len(operaciones)

    # 3. Crear e iniciar los procesos trabajadores (calculadoras)
    num_workers = 4
    procesos = []
    for i in range(num_workers):
        proceso = multiprocessing.Process(target=calculadora_worker, args=(cola_de_tareas, cola_de_resultados), name=f"Calculadora-{i+1}")
        procesos.append(proceso)
        proceso.start()

    # 4. Distribuir las tareas a los trabajadores a través de la cola
    for op in operaciones:
        cola_de_tareas.put(op)

    # 5. Enviar señales de parada a los trabajadores (una por cada trabajador)
    for _ in range(num_workers):
        cola_de_tareas.put(None)

    # 6. Recoger y mostrar los resultados
    print("\n--- Resultados de los Cálculos ---")
    for _ in range(num_tareas):
        resultado = cola_de_resultados.get()
        print(f"[Proceso Principal] Resultado recibido: {resultado}")

    print("\n[Proceso Principal] Todos los cálculos han finalizado.")