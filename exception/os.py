import os
print os.getcwd()
if os.path.exists('adiil'):
    print "hii"
else:
    os.mkdir('adiil')
    os.chdir('newmdr')

