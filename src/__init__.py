from os import path, getcwd, chdir

def printMyPath(_type = 2):
    print('0: cwd:     {}'.format(getcwd()))
    print('1: __file__:{}'.format(__file__))
    print('2: abspath: {}'.format(path.abspath(__file__)))
    if _type == 0:
        return getcwd()
    elif _type == 1:
        return __file__
    elif _type == 2:
        return path.abspath(__file__)