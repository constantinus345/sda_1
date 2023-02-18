import ax
import time

start_exec = time.perf_counter()

for a in range(100,200):
    for b in range(50,70):
        rez = ax.sum(a,b)
        print(f"rez = {rez}")



print(f"Timpul de executie a fost = {time.perf_counter()-start_exec} secunde")