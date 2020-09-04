"""sftp client"""
from sshClient import CustomSSHClient


class SFTPClient(CustomSSHClient):
    def __init__(self, host, port, user, pwd):
        super().__init__(host, port, user, pwd)  # invoke base class __init__
        self.sftp = self.ssh.open_sftp()

    def upload(self, src, dest):
        self.sftp.put(src, dest)
        print(f'{src} uploaded as {dest}')

    def __del__(self):
        self.sftp.close()
        super().__del__()


if __name__ == '__main__':
    ftp = SFTPClient('13.126.143.155', 22, 'training', 'training')
    ftp.upload('inheritence.py', 'InheritanceMultiple.py')
    print(ftp.check_output('ls -l'))
