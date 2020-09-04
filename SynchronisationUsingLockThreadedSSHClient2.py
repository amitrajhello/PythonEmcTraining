"""demo for the sync using lock"""

import threading
import logging
from time import sleep
import pyexcel
from sshClient import CustomSSHClient

logging.basicConfig(format='%(threadName)s : %(message)s')  # config the logger
target_file = 'sshresponse.log'


class ThreadedSSHClient(CustomSSHClient):
    lock = threading.Lock()  # class variable,  # sync using lock

    def __init__(self, host, port, user, pwd, job):
        super().__init__(host, port, user, pwd)  # invoke base class __init__
        self.job = job
        self.t_name = threading.current_thread().name
        self.task_runner()

    def task_runner(self):
        payload = self.check_output(self.job)
        caption = f'{self.t_name} ran {self.job} @ {self.host}'

        logging.warning('waiting for the lock')

        with ThreadedSSHClient.lock:
            logging.warning('acquired the lock')

            with open(target_file, 'a') as fw:
                """critical section"""
                sleep(1)
                logging.warning('done with the critical section')
                fw.write(caption.center(80, '-') + '\n')
                fw.write(payload + '\n')

            logging.warning('releases the lock')


def main():
    sheet = pyexcel.get_sheet(file_name=r'C:\Users\raja6\Desktop\study\emc python training\hosts.xlsx')

    for ssh_host_info in sheet:
        t = threading.Thread(target=ThreadedSSHClient, args=ssh_host_info)
        t.start()


if __name__ == '__main__':
    main()
