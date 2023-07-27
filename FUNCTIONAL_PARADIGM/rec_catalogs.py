import os
# Recursive control of content inside directories

path = 'C:\\Users\Назар\Favorites\Desktop\PYTHON\EGOROV_CHANNEL_YOUTUBE'
filename = 'tuple.py'

def FileControl(path, filename, level=1):
    print('Level = ', level, 'Content: ', os.listdir(path))

    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            print()
            print('Go down', path + '\\' + i)
            FileControl(path + '\\' + i, level + 1)
            print('Come back', path)
                
FileControl(path, filename)
    