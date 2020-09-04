"""single thread ssh client"""

import paramiko


class CustomSSHClient:
    def __init__(self, host, port, user, pwd):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, self.port, self.user, self.pwd)

    def check_output(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        output = stdout.read()
        payload = output if output else stderr.read()
        return payload.decode()  # bytes to str

    def __del__(self):
        self.ssh.close()


if __name__ == '__main__':
    ssh = CustomSSHClient('13.126.143.155', 22, 'training', 'training')
    op = ssh.check_output('free -m')
    print(op)
