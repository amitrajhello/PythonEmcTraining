import threading
import pyexcel


def main():
    sheet = pyexcel.get_sheet(file_name=r'C:\Users\raja6\Desktop\study\emc python training\hosts.xlsx')
    for ssh_host_info in sheet:
        print(ssh_host_info)


if __name__ == '__main__':
    main()
