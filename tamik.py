import os, time

cmd = input("Введите команду: ")
start = time.time()        
os.system(cmd)             
end = time.time()          

print(f"⏱ Время выполнения: {end - start:.3f} сек.")