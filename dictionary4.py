info = {
    'host': 'ws1',
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2
}

# lookup or read value from key

print(info['host'])
print(info['domain'])
# print(info['apps'])
print()
print(info.get('app'))
print(info.get('apps'))
print()
print(info.get('app', 'apache tomcat'))
print(info.get('apps', 'apache tomcat'))


