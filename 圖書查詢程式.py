import tkinter as tk
import sqlite3
import pandas as pd
conn=sqlite3.connect('111')
conn.cursor()
sql = "select * from table1"
df = pd.read_sql (sql,conn,)
aa= pd.DataFrame (df)

window = tk.Tk()
window.title('圖書主頁面')
window.geometry('1000x600')



# 查詢頁
def e():
    window1 = tk.Toplevel()
    window1.title('查詢')
    window1.geometry('1000x600')
    var2 = tk.StringVar()
    lb = tk.Listbox(window1, listvariable=var2)
    list_items = ['書碼', '書名', '作者']
    for item in list_items:
        lb.insert('end', item)
    lb.place(x=300, y=50, anchor='n')

    ab = tk.Entry(window1, show=None,width=50)
    ab.place(x=400, y=50, anchor='nw')
    def A():
        try:
            A7.delete('1.0', 'end')
            A8.delete('1.0', 'end')
            A9.delete('1.0', 'end')
            var = ab.get()
            B = lb.get(lb.curselection())

            if B == '書碼':
                ac = int(var)
                D = aa[aa['書碼'] == ac]
                E=D.ix[0]
                F=(E.ix[0])
                I=(E.ix[1])
                J=(E.ix[2])
                A7.insert(1.0, F)
                A8.insert(1.0, I)
                A9.insert(1.0, J)
            elif B == '書名':
                ad = str(var)
                D = aa[aa['書名'] == ad]
                E = D.ix[0]
                F = (E.ix[0])
                I = (E.ix[1])
                J = (E.ix[2])
                A7.insert(1.0, F)
                A8.insert(1.0, I)
                A9.insert(1.0, J)
            elif B == '作者':
                ad = str(var)
                D = aa[aa['作者'] == ad]
                for a in range(len(D)):
                    E = D.ix[a]
                    F = (E.ix[0])
                    I = (E.ix[1])
                    J = (E.ix[2])
                    A7.insert('end', str(F)+'\n')
                    A8.insert('end', str(I)+'\n')
                    A9.insert('end', str(J)+'\n')


        except:
            A7.insert('end', ' 無此資料或無點選查詢方式')

    A1=tk.Label(window1, text='查詢方式').place(x=300,y=50,anchor='s')
    A2=tk.Label(window1,text='輸入區').place(x=400,y=50,anchor='sw')
    A3=tk.Label(window1, text='顯示區').place(x=400, y=100, anchor='sw')
    A4=tk.Label(window1, text='書碼').place(x=400, y=120, anchor='sw')
    A5=tk.Label(window1, text='書名').place(x=550, y=120, anchor='sw')
    A6=tk.Label(window1, text='作者').place(x=700, y=120, anchor='sw')
    A7=tk.Text(window1,width=20,height=15)
    A7.place(x=400,y=120,anchor='nw')
    A8=tk.Text(window1, width=20, height=15)
    A8.place(x=550, y=120, anchor='nw')
    A9=tk.Text(window1, width=20, height=15)
    A9.place(x=700, y=120, anchor='nw')
    A10=tk.Button(window1,text='查詢',bg='blue' ,width=20, height=3,command=A).place(x=770, y=40, anchor='nw')
    A11=tk.Label(window1, text='查書區',font=('Arial', 60),bg='red').place(x=400, y=530, anchor='sw')







a=tk.Button(window,text='查詢',width=30,height=3,font=('Arial', 16),command=e).place(x=320,y=30,anchor='nw')


canvas0=tk.Canvas(window,width=600,height=250)
canvas0.place(x=400,y=300,anchor='ne')

canvas=tk.Canvas(window,width=600,height=250)
image_file=tk.PhotoImage(file='111.gif')
image=canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.place(x=200,y=300,anchor='nw')


window.mainloop()

canvas0=tk.Canvas(window,width=600,height=250)
canvas0.place(x=400,y=300,anchor='ne')

canvas=tk.Canvas(window,width=600,height=250)

canvas.place(x=390,y=300,anchor='nw')


window.mainloop()


