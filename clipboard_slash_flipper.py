
from Tkinter import Tk # for Python 2.x

clipboard = Tk().clipboard_get()
clipboard = clipboard.replace('//', '/')
clipboard = '{}{}'.format(clipboard[:2], clipboard[2:].replace('\\\\', '\\'))
clipboard = clipboard.replace('/', '\\')

# forward = [i for i in clipboard if i == '/']
# backward = [i for i in clipboard if i == '\\']

# if len(forward) > len(backward):
#     clipboard = clipboard.replace('/', '\\')
# else:
#     clipboard = clipboard.replace('\\', '/')

Tk().clipboard_clear()
Tk().clipboard_append(clipboard)

print(Tk().clipboard_get())
