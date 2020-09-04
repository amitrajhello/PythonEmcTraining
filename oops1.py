import os
import sys
import math
import pprint

class SystemInformation:
    pass


# pass to define dummy code block
if __name__ == '__main__':
    si = SystemInformation()
    print(si)
    print(SystemInformation)
    print(__name__)  # default ns
    print(os.__name__)
    print(math.__name__)
    print(pprint.PrettyPrinter)
