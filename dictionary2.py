info = {
    'host': 'ws1',
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2
}
print(info)  # printing the dictionary 
item = 'version'

if item in info:  # validate
    info[item] = 3.6  # update

info['arch'] = 'x86_64'  # add an element to the dictionary
print(info)
