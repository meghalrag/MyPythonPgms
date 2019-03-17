import os
import shutil
print os.getcwd()
if os.path.exists('newmdr'):
    pass
    os.chdir('newmdr')
    # os.rename('newmdr','newmdr1')
    f = open('changefile.txt', 'w', 1)
    f.write('')
    # inp = raw_input("input:")
    # inp = inp + '\n'
    # f.write(inp)
    # print os.name
    #create dir in current folder
    # os.mkdir('mkdirsample')
    # create folder with path
    # os.makedirs('G:/workspace/pythonpgm/filepgm/hello')
    # os.makedirs('G:/hello')
    #view folders
    # for i in os.listdir('/media/meghal/New Volume'):
    #     print i
    #move folder
    # string=raw_input("enter the fodler name to move: ")
    # spath=''
    # source=os.path.join('G:\\',string)
    # destination=os.path.join('H:\\',string)
    # shutil.move(source,destination)
    #copy and paste folder
    # shutil.copytree('H:\\hello','G:\\hello')
    # copy and paste file
    # shutil.copy('H:\\hello\\sample.txt','G:\\hello')
    #shutdown system
    # check = raw_input("Want to 1.shutdown/2.restart your computer ? (y/n): ");
    # if check == 'n':
    #     exit()
    # elif check=='1':
    #     os.system("shutdown /s /t 20")
    # elif check=='2':
    #     os.system("shutdown /r /t 10")
    #close an application
    # os.system("taskkill /f /im notepad.exe")
    # os.system("taskkill /f /im chrome.exe")
    # os.system("taskkill /f /im pycharm64.exe")
    #delete directory
    # os.remove('ospgm.py')
    # os.rmdir('newmdr')
    # shutil.rmtree('newmdr')

else:
    os.mkdir('newmdr')
    print "run again"