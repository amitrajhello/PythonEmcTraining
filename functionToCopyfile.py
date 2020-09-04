import os
def copy(src_file, dest_file):
    """to perform the file copy"""
    content = open(src_file).read()
    open(dest_file, 'w').write(content)


copy('passwd.txt', 'passwd-copy.txt')

#os.unlink('passwd-copy.txt')    to delete a file after importing os module

