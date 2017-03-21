import os

specify_str = 'mydict'

def rela_path(dirname):
    results = []
    for root, dirs, files in os.walk(dirname):
        results += [os.path.relpath(os.path.join(root, x), start=dirname) for x in files if specify_str in x]

    for result in results:
        print(result)

rela_path(os.getcwd())  # os.getcwd()返回当前的目录