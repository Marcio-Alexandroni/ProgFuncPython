import threading
import random
import time

def sensor_temperatura():
    for i in range(5):
        temp = random.uniform(15.0, 35.0)
        print(f'[Temperatura] --> leitura {i+1} --> {temp:.2f}ºC')
        time.sleep(1)
    
def sensor_umidade():
    for i in range(5):
        umidade = random.uniform(30.0, 90.0)
        print(f'[Umidade] --> leitura {i+1} --> {umidade:.2f}%')
        time.sleep(1)
    
def sensor_ar():
    for i in range(5):
        qualidade = random.uniform(0, 200)
        print(f'[Qualidade do Ar] --> leitura {i+1} --> {qualidade:.2f} AQI')
        time.sleep(1)
    
# Programa Principal --> criação das Threads
t1 = threading.Thread(target=sensor_temperatura)
t2 = threading.Thread(target=sensor_umidade)
t3 = threading.Thread(target=sensor_ar)

# Início das Threads
t1.start()
t2.start()
t3.start()

# Concorrência: todos os processos estão concorrendo pelo mesmo processador.
# Paralelismo: dois processadores (em ex) ou núcleos processam (ou agem) ao mesmo tempo.