# -*- coding: utf-8 -*-
'''
This is a scrpit for Download Bilibili-viedios Cover
Author: Jachin
Data: 2017- 11- 07
'''

import crawbilibili
from Tkinter import * # 导入Tkinter模块
from PIL import Image,ImageTk
import tkinter.messagebox
import tkinter.filedialog

root = Tk()
root.resizable(0,0)
root.title('Get Cover')
root.geometry('336x130')

canvas = Canvas(root,bg='gray')
image = Image.open("ico.jpg")
im = ImageTk.PhotoImage(image)
canvas.create_image(60, 50,anchor = 'center', image=im)
canvas.create_text(60,100,text = '获取封面',fill = 'black',font = (u'幼圆',14,'bold'))
canvas.create_text(62,102,text = '获取封面',fill = 'gray',font = (u'幼圆',14,'bold'))
canvas.place(relx=0.020, rely=0.062, relwidth=0.37, relheight=0.88)

var = StringVar()
var = '输入av号，如:av123'
var = ''
label1 = Label(root,text = var,font = ('幼圆',10))
label1.place(relx=0.452, rely=0.32, relwidth=0.479, relheight=0.254)

Text1Var = StringVar(value='')
Text1 = Entry(root, textvariable=Text1Var, font=(u'黑体',14))
Text1.place(relx=0.452, rely=0.102, relwidth=0.479, relheight=0.254)

path = r'E:\av'
def do():
    global path
    path = tkinter.filedialog.askdirectory()

Command1 = Button(root, text=u'打开', command=do,font=(u'幼圆',14,'bold'),relief = 'groove')
Command1.place(relx=0.455, rely=0.532, relwidth=0.217, relheight=0.377)

def Save():
    number = Text1.get() or '123'
    try:
        print path
        crawbilibili.saveImg(number,path)
        tkinter.messagebox.showinfo('提示', '成功了')
    except:
        tkinter.messagebox.showinfo('错误', '罢工了')

Command2 = Button(root, text=u'确认', command=Save,font=(u'幼圆',14,'bold'),relief = 'groove')

Command2.place(relx=0.725, rely=0.532, relwidth=0.217, relheight=0.377)
'''
待完成功能：回车与确认按键绑定
Command2.bind('<Return>',Save())
Command2.focus_set()
'''

root.mainloop()
