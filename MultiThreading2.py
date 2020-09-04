import threading
import time
from random import random


def worker(delay):
    """thread funtion"""
    t_name = threading.current_thread().name
    t_id = threading.current_thread().ident
    time.sleep(delay)
    print(t_name, 'waited for : ', delay)


def main():
    """main thread function"""

    for item in range(1, 6):
        rand_value = random()
        t = threading.Thread(target=worker, args=(rand_value,), name=f't{item}')
        t.start()

    print(threading.current_thread().name, 'prepare to terminates')


if __name__ == '__main__':
    main()
