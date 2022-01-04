import os


def directory_check(path: str):
    if os.path.isdir(path):
        print(f'Directory check: {path}')
        for i in os.walk(path):
            print(i)
        for i in os.listdir(path):
            for n in os.walk(path + '/' + i):
                print(n)
    elif os.path.isfile(path):
        print('Please specify the path to the directory')
    return


directory_check('/home/oleh/Study')
