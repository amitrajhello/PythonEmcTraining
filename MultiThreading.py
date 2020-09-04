import threading


def worker():
    """thread funtion"""
    t_name = threading.current_thread().name
    t_id = threading.current_thread().ident
    print(t_name, ':', t_id)


def main():
    """main thread function"""

    for item in range(1, 6):
        t = threading.Thread(target=worker)
        t.start()

    print(threading.current_thread().name, 'prepare to terminates')


if __name__ == '__main__':
    main()

