"""scopes in python"""

n = 100  # global scope


def demo():
    n = 'pip'
    print(n)


demo()
print(n)

