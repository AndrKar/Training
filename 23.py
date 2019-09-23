import os
from datetime import datetime

print(os.getcwd())
os.makedirs('OS-demo2\\SubDir-2')
os.rename('text.txt', 'demo.txt')
print(os.stat('demo.txt'))
print(os.stat('demo.txt').st_size)
print(os.stat('demo.txt').st_mtime)
mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))
print(os.listdir())

for dirpath, dirnames, filenames in os.walk('c:\\Users\\Olga\\Documents\\Andrii\\Python'):
    print('Current path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)
    print()

os.chdir('c:\\Users\\Olga\\Desktop')
print(os.getcwd())

print(os.getenv('HOME'))
