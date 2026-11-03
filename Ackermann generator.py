from tkinter import *
from tkinter import ttk

resuR = 0
resuL = 0

def clicked():
    fun1 = box.get()
    fun2 = box2.get()
    fun3 = box3.get()
    resuR = "Roll < 0 ? atan(1/((1/tan(-Roll*" + str(fun1) + "))+(" + str(fun2) + "/" + str(fun3) + ")))/-" + str(fun1) + ":Roll"
    resuL = "Roll > 0 ? atan(1/((1/tan(Roll*" + str(fun1) + "))+(" + str(fun2) + "/" + str(fun3) + ")))/" + str(fun1) + ":Roll"
    resu1.insert(0, resuR)
    resu1.pack(padx=50, pady=20, anchor="w",fill="x", expand=True)
    resu2.insert(0, resuL)
    resu2.pack(padx=50, pady=20, anchor="w",fill="x", expand=True)
app = Tk()
resu1 = Entry(app)
resu2 = Entry(app)
app.geometry("500x300")
app.title("Ackermann funky generator")
#ここにコードを書く
label = ttk.Label(app,text='Ackermann funky generator\nアッカーマンアングル再現funky treesジェネレータ')
label.pack()
lab1 = ttk.Label(app,text='max steer angle 最大ステア角')
box = ttk.Entry(app)
lab1.pack()
lab2 = ttk.Label(app,text='Wheel Base ホイールベース')
box2 = ttk.Entry(app)
lab2.pack()
lab3 = ttk.Label(app,text='LR wheel base 左右タイヤ間の距離')
box3 = ttk.Entry(app)
lab3.pack()
button =ttk.Button(app,text='OK',command=clicked)
box.pack()
box2.pack()
box3.pack()
button.pack()
app.mainloop()
