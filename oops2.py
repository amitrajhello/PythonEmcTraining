class SystemInformation:
    def __init__(self):  # constructor
        print(self, 'am in constructor')

    def __del__(self):  # destructor
        print(self, 'getting destroyed')


if __name__ == '__main__':  # main method
    si = SystemInformation()
    print(si)



