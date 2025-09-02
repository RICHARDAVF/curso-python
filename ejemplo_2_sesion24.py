import multiprocessing
import random
def worker(counter,array,lock):
    process_id = multiprocessing.current_process().name
    for _ in range(5000):
        with lock:
            counter.value+=1
            index = random.randint(0,len(array)-1)
            array[index]+=1
    print(f"Proceso con id: {process_id} finalizado")    
if __name__ == "__main__":
    shared_lock = multiprocessing.Lock()
    shared_counter = multiprocessing.Value('i',0)
    shared_array = multiprocessing.Array('i',100)
    num_process = 4
    procesos = []
    print(f"Iniciando {num_process} procesos para modificar la memoria compartida")
    for i in range(num_process):
        p = multiprocessing.Process(target=worker,args=(shared_counter,shared_array,shared_lock))
        procesos.append(p)
        p.start()
    for p in procesos:
        p.join()
    counter_esperado = num_process*5000
    suma_total = sum(shared_array)
    
    print(f"Valor final del contador: {shared_counter.value} esperado {counter_esperado}")
    print(f"SUma total del array : {suma_total }( esperado :{counter_esperado})")
    
    # [1,1,1,1,]+[1,1,1,1,]+[1,1,1,1,]+[1,1,1,1,]