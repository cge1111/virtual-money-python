# 09-3 프로세스와 스레드 기초
# multiprocessing 모듈

import multiprocessing as mp
import time

def worker():
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)
    time.sleep(5)
    print("SubProcess End")


if __name__ == "__main__":
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)

    p = mp.Process(name = "SubProcess", target= worker)
    p.start()

    print("MainProcess End")