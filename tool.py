import os
import os.path

pwd = './'


def listUiFile():
    ui = []
    files = os.listdir(pwd)
    for filename in files:
        if os.path.splitext(filename)[1] == '.ui':
            ui.append(filename)
    return ui


def transPyFile(filename):
    return os.path.splitext(filename)[0] + '.py'


def runMain():
    ui = listUiFile()
    for uiFile in ui:
        pyFile = transPyFile(uiFile)
        cmd = 'pyuic5 -o {} {}'.format(pyFile, uiFile)
        os.system(cmd)
        print(cmd)


runMain()
