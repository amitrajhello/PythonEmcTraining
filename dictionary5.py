info = {
    'host': 'ws1',
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2
}
# iterate a dict, key, val pair

for key, value in info.items():  # printing key value pair
    print(key, ':', value)

print()

for x in info:  # printing only key by default
    print(x)
