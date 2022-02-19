import time

from cefpython3 import cefpython as cef
from tkinter import *
import tkinter as tk
import threading
import sys

window = tk.Tk()
window.title('主頁面')
window.geometry('1000x600')

counties = []



###鑲入網頁
# cefpython3 目前只支持python3.7，高版本Python不兼容
def embed_browser_thread(frame, _rect):
    sys.excepthook = cef.ExceptHook
    window_info = cef.WindowInfo(frame.winfo_id())
    window_info.SetAsChild(frame.winfo_id(), _rect)
    cef.Initialize()
    cef.CreateBrowserSync(window_info, url='file:///D:/Data/python/class/presentetion/TESTPOSTGIS/map.html')
    cef.MessageLoop()







def e(counties):
    time.sleep(2)
    import plot
    plot.map(counties)
    root = Tk()
    root.title('map')
    root.geometry("800x600")

    frame1 = Frame(root, bg='blue', height=600)
    frame1.pack(side=TOP, fill=X)

    frame2 = Frame(root, bg='white', height=600)
    frame2.pack(side=TOP, fill=X)

    rect = [0, 0, 800, 600]
    thread = threading.Thread(target=embed_browser_thread, args=(frame1, rect))
    thread.start()

    root.mainloop()
def a1():
    b=measureSystem1.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties
def a2():
    b=measureSystem2.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties
def a3():
    b=measureSystem3.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties
def a4():
    b=measureSystem4.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties

def a5():
    b=measureSystem5.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties
def a6():
    b=measureSystem6.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties

def a7():
    b=measureSystem7.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties
def a8():
    b=measureSystem8.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties

def a9():
    b=measureSystem9.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties
def a10():
    b=measureSystem10.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties

def a11():
    b=measureSystem11.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties
def a12():
    b=measureSystem12.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties

def a13():
    b=measureSystem13.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties
def a14():
    b=measureSystem14.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties

def a15():
    b=measureSystem15.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties

def a16():
    b=measureSystem16.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties

def a17():
    b=measureSystem17.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties
def a18():
    b=measureSystem18.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties
def a19():
    b=measureSystem19.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties

def a20():
    b=measureSystem20.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties

def a21():
    b=measureSystem21.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties
def a22():
    b=measureSystem22.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties
def a23():
    b=measureSystem23.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties

def a24():
    b=measureSystem24.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties
def a25():
    b=measureSystem25.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties
def a26():
    b=measureSystem26.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties
def a27():
    b=measureSystem27.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties
def a28():
    b=measureSystem28.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties
def a29():
    b=measureSystem29.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties
def a30():
    b=measureSystem30.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties
def a31():
    b=measureSystem31.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties
def a32():
    b=measureSystem32.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties
def a33():
    b=measureSystem33.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties
def a34():
    b=measureSystem34.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties

def a35():
    b=measureSystem35.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties

def a36():
    b=measureSystem36.get()
    print(b)

    c=str(b.split(b[1])[0])
    print(c)
    d=str(b.split(b[0])[1])
    if c== '1':
        print(2)
        counties.append(d)
        print(counties)
    else:
        try:
            counties.remove(d)
        except:
            counties
creatvar=locals()
ls=range(1,38)
for i,s in enumerate(ls):
    creatvar['measureSystem'+str(i)]=s
    creatvar['measureSystem' + str(i)]=StringVar()
    creatvar['measureSystem' + str(i)].set(False)


check1 = tk.Checkbutton(window, text='鳳山區',command=a1, variable=measureSystem1,onvalue='1鳳山區', offvalue='0鳳山區').place(x=100,y=170,anchor='nw')
check2 = tk.Checkbutton(window, text='鹽埕區',command=a2, variable=measureSystem2,onvalue='1鹽埕區', offvalue='0鹽埕區').place(x=100,y=200,anchor='nw')
check3 = tk.Checkbutton(window, text='鼓山區',command=a3, variable=measureSystem3,onvalue='1鼓山區', offvalue='0鼓山區').place(x=100,y=230,anchor='nw')
check4 = tk.Checkbutton(window, text='林園區',command=a4, variable=measureSystem4,onvalue='1林園區', offvalue='0林園區').place(x=100,y=260,anchor='nw')
check5 = tk.Checkbutton(window, text='大寮區',command=a5, variable=measureSystem5,onvalue='1大寮區', offvalue='0大寮區').place(x=100,y=290,anchor='nw')
check6 = tk.Checkbutton(window, text='左營區',command=a6, variable=measureSystem6,onvalue='1左營區', offvalue='0左營區').place(x=100,y=320,anchor='nw')
check7 = tk.Checkbutton(window, text='大樹區',command=a7, variable=measureSystem7,onvalue='1大樹區', offvalue='0大樹區').place(x=100,y=350,anchor='nw')
check8 = tk.Checkbutton(window, text='楠梓區',command=a8, variable=measureSystem8,onvalue='1楠梓區', offvalue='0楠梓區').place(x=100,y=380,anchor='nw')
check9 = tk.Checkbutton(window, text='大社區',command=a9, variable=measureSystem9,onvalue='1大社區', offvalue='0大社區').place(x=100,y=410,anchor='nw')
check10 = tk.Checkbutton(window, text='三民區',command=a10, variable=measureSystem10,onvalue='1三民區', offvalue='0三民區').place(x=100,y=440,anchor='nw')
check11 = tk.Checkbutton(window, text='仁武區',command=a11, variable=measureSystem11,onvalue='1仁武區', offvalue='0仁武區').place(x=100,y=470,anchor='nw')
check12 = tk.Checkbutton(window, text='新興區',command=a12, variable=measureSystem12,onvalue='1新興區', offvalue='0新興區').place(x=100,y=500,anchor='nw')
check13 = tk.Checkbutton(window, text='前金區',command=a13, variable=measureSystem13,onvalue='1前金區', offvalue='0前金區').place(x=100,y=530,anchor='nw')
check14 = tk.Checkbutton(window, text='鳥松區',command=a14, variable=measureSystem14,onvalue='1鳥松區', offvalue='0鳥松區').place(x=100,y=560,anchor='nw')
check15 = tk.Checkbutton(window, text='岡山區',command=a15, variable=measureSystem15,onvalue='1岡山區', offvalue='0岡山區').place(x=200,y=170,anchor='nw')
check16 = tk.Checkbutton(window, text='苓雅區',command=a16, variable=measureSystem16,onvalue='1苓雅區', offvalue='0苓雅區').place(x=200,y=200,anchor='nw')
check17 = tk.Checkbutton(window, text='前鎮區',command=a17, variable=measureSystem17,onvalue='1前鎮區', offvalue='0前鎮區').place(x=200,y=230,anchor='nw')
check18 = tk.Checkbutton(window, text='橋頭區',command=a18, variable=measureSystem18,onvalue='1橋頭區', offvalue='0橋頭區').place(x=200,y=260,anchor='nw')
check19 = tk.Checkbutton(window, text='燕巢區',command=a19, variable=measureSystem19,onvalue='1燕巢區', offvalue='0燕巢區').place(x=200,y=290,anchor='nw')
check20 = tk.Checkbutton(window, text='旗津區',command=a20, variable=measureSystem20,onvalue='1旗津區', offvalue='0旗津區').place(x=200,y=320,anchor='nw')
check21 = tk.Checkbutton(window, text='田寮區',command=a21, variable=measureSystem21,onvalue='1田寮區', offvalue='0田寮區').place(x=200,y=350,anchor='nw')
check22 = tk.Checkbutton(window, text='小港區',command=a22, variable=measureSystem22,onvalue='1小港區', offvalue='0小港區').place(x=200,y=380,anchor='nw')
check23 = tk.Checkbutton(window, text='阿蓮區',command=a23, variable=measureSystem23,onvalue='1阿蓮區', offvalue='0阿蓮區').place(x=200,y=410,anchor='nw')
check24 = tk.Checkbutton(window, text='路竹區',command=a24, variable=measureSystem24,onvalue='1路竹區', offvalue='0路竹區').place(x=200,y=440,anchor='nw')
check25 = tk.Checkbutton(window, text='湖內區',command=a25, variable=measureSystem25,onvalue='1湖內區', offvalue='0湖內區').place(x=200,y=470,anchor='nw')
check26 = tk.Checkbutton(window, text='茄萣區',command=a26, variable=measureSystem26,onvalue='1茄萣區', offvalue='0茄萣區').place(x=200,y=500,anchor='nw')
check27 = tk.Checkbutton(window, text='永安區',command=a27, variable=measureSystem27,onvalue='1永安區', offvalue='0永安區').place(x=200,y=530,anchor='nw')
check28 = tk.Checkbutton(window, text='彌陀區',command=a28, variable=measureSystem28,onvalue='1彌陀區', offvalue='0彌陀區').place(x=200,y=560,anchor='nw')
check29 = tk.Checkbutton(window, text='梓官區',command=a29, variable=measureSystem29,onvalue='1梓官區', offvalue='0梓官區').place(x=300,y=170,anchor='nw')
check30 = tk.Checkbutton(window, text='旗山區',command=a30, variable=measureSystem30,onvalue='1旗山區', offvalue='0旗山區').place(x=300,y=200,anchor='nw')
check31 = tk.Checkbutton(window, text='美濃區',command=a31, variable=measureSystem31,onvalue='1美濃區', offvalue='0美濃區').place(x=300,y=230,anchor='nw')
check32 = tk.Checkbutton(window, text='六龜區',command=a32, variable=measureSystem32,onvalue='1六龜區', offvalue='0六龜區').place(x=300,y=260,anchor='nw')
check33 = tk.Checkbutton(window, text='甲仙區',command=a33, variable=measureSystem33,onvalue='1甲仙區', offvalue='0甲仙區').place(x=300,y=290,anchor='nw')
check34 = tk.Checkbutton(window, text='杉林區',command=a34, variable=measureSystem34,onvalue='1杉林區', offvalue='0杉林區').place(x=300,y=320,anchor='nw')
check35 = tk.Checkbutton(window, text='內門區',command=a35, variable=measureSystem35,onvalue='1內門區', offvalue='0內門區').place(x=300,y=350,anchor='nw')
check36 = tk.Checkbutton(window, text='桃源區',command=a36, variable=measureSystem36,onvalue='1桃源區', offvalue='0桃源區').place(x=300,y=380,anchor='nw')






a=tk.Button(window,text='查詢',width=30,height=3,font=('Arial', 16),command=lambda:e(counties)).place(x=320,y=30,anchor='nw')##查詢鍵


window.mainloop()
