
# -*- coding: UTF-8 -*-

import os
from excel import *
from tkinter import *

files = []
path = r'E:\project\src\mtt'


def loadFile():
    for filename in os.listdir(path):
        print(os.path.join(path, filename))
        files.append(filename)


loadFile()
root = Tk()
root.title("测试测试")

# 是x 不是*
root.geometry('400x300')
root.resizable(width=False, height=False)


frame = Frame(root)
frame.pack()


fline = Frame(frame)
fline.pack()
Label(fline, text='选择文件').pack(side='left')

v = StringVar(fline)
OptionMenu(fline, v, *files).pack(side='right')
v.set(files[0])


def createFile():
    print(v.get())
    CreateExcel(path+'/'+v.get())


def compareResult():
    print(v.get())
    CreateResult(v.get())


btn_create = Button(frame, text="生成文件", width=15, command=createFile)
btn_create.pack()
Button(frame, text="比对结果", width=15, command=compareResult).pack()

# 进入消息循环
root.mainloop()
