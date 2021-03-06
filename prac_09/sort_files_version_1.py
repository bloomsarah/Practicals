"""Use os.mkdir() to create a directory with for each new extension that your program finds and use shutil.move() to
move files into these new directories. Do not try and create directories you have already made. Add the extensions to
a list or a set as your process the files. """

import os
import shutil

extensions = []
os.chdir('FilesToSort')
print(os.getcwd())
print(os.listdir('.'))

for filename in os.listdir('.'):
    p = "{}/{}".format(os.getcwd(), filename)
    extension = os.path.splitext(p)
    extensions.append(extension[1])
extensions_set = set(extensions)
print(extensions_set)

for extension in extensions_set:
    os.mkdir(extension)

for filename in os.listdir('.'):
    p = "{}/{}".format(os.getcwd(), filename)
    extension = os.path.splitext(p)
    if extension[1]:
        pass


