# Given a directory, find out the file Name having max size recursively

import glob ## DIR equivalent command in Python
import os.path
import time

## Decorator without Argument
# def mea(fun):
#         def _inner1(*args, **kwargs): # args = (path,)
#             st = time.time()
#             res = fun(*args, **kwargs)  # fun = getMaxFilename(path)
#             print("Time taken", round(time.time()-st,precesion), "secs")
#             return res
#         return _inner1

### Decorator with Input argument (will result into 2 inner functions)
def mea(precesion):
    def _inner1(fun): #fun = getMaxFilename
        def _inner2(*args, **kwargs): # args = (path,)
            st = time.time()
            res = fun(*args, **kwargs)  # fun = getMaxFilename(path)
            print("Time taken", round(time.time()-st,precesion), "secs")
            return res
        return _inner2
    return _inner1

@mea(6)
def getMaxFilename(path): # getMaxFilename  ==> mea(getMaxFilename) due to decorator
    def get_files(path, ed={}):
        files = glob.glob(os.path.join(path, "*"))
        for file in files:
            if os.path.isfile(file):
                ed[file] = os.path.getsize(file)
        for file in files:
            if not os.path.isfile(file):
                get_files(file, ed)
        return ed

    allfiles = get_files(path)
    sted = sorted(allfiles, key=lambda k: allfiles[k])
    return sted[-1] if sted else ''

### Dcorator Hands on
# if __name__ == '__main__':
#     path = r"C:\Users\shyam\PycharmProjects\DS_training"
#     print(getMaxFilename(path))  #_inner2(path)


#Given a directory, return all files in that dir recursively
# Normal Function
def get_files(path, res):
    files = glob.glob(os.path.join(path, "*"))
    for file in files:
        if os.path.isfile(file):
            res.append(file)
    for file in files:
        if not os.path.isfile(file):
            get_files(file, res)
    return res

## Iterator Function
def get_files_iter(path):
    files = glob.glob(os.path.join(path, "*"))
    for file in files:
        if os.path.isfile(file):
            yield file
    for file in files:
        if not os.path.isfile(file):
            yield from get_files_iter(file)

# if __name__ == '__main__':
#     path = r"C:\Users\shyam\PycharmProjects\DS_training"
#     for f in get_files_iter(path):
#         print(f)

## using class creating Inbuilt Iterator using dunder method

class Files:
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        files = glob.glob(os.path.join(self.path, "*"))
        for file in files:
            if os.path.isfile(file):
                yield file
        for file in files:
            if not os.path.isfile(file):
                yield from Files(file)


if __name__ == '__main__':
    path = r"C:\windows\system32"
    for f in Files(path):
        print(f)