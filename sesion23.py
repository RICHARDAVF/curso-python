import multiprocessing
import time

def worker_process():
    """Función que simula una tarea ejecutada por un proceso."""
    print(f"Proceso hijo iniciado: {multiprocessing.current_process().name}")
    time.sleep(2)
    print(f"Proceso hijo finalizado: {multiprocessing.current_process().name}")


if __name__ == "__main__":
    print(f"Proceso principal iniciado: {multiprocessing.current_process().name}")

    processes = []
    num_processes = 2

    # Crear y almacenar los procesos
    for i in range(num_processes):
        process = multiprocessing.Process(
            target=worker_process
            ,name=f"Proceso {i + 1}"
        )
        processes.append(process)
        process.start() # Iniciar el proceso

    # Esperar a que todos los procesos terminen
    for process in processes:
        process.join()

    print("Todos los procesos hijos han finalizado. El programa principal termina.")
