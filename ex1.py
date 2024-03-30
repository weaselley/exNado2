##############################
## contents
## 01. Basic frame
## 02. Button
## 03. label
## 04. text and entry
## 05. list box
## 06. Check button
## 07. Radio button
## 08. Combo box
## 09. progress bar
## 10. menu
## 11. message box
## 12. frame
## 13. scroll bar
## 14. grid
##############################
## 01. Basic frame
# from tkinter import *
# root = Tk()
# root.title("pGUI")
# root.geometry("640x480")
# # root.geometry("640x480+500+300")  # x, y coordination
# root.resizable(False, False) # x(width), y(height)
# root.mainloop()

##############################
## 02. Button
# from tkinter import *
# import os

# root = Tk()
# root.title("pGUI")

# btn1 = Button(root, text="버튼1")
# btn1.pack()
# btn2 = Button(root, padx=5, pady=10, text="버튼2")
# btn2.pack()
# btn3 = Button(root, padx=10, pady=5, text="버튼3")
# btn3.pack()
# btn4 = Button(root, width=10, height=3, text="버튼4")
# btn4.pack()
# btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
# btn5.pack()
# curr_dir_path = os.path.dirname(os.path.abspath(__file__))
# file_path = curr_dir_path + '/userlib_pic/check.png'
# photo = PhotoImage(file=file_path)
# btn6 = Button(root, image=photo)
# btn6.pack()
# def btncmd():
#     print("버튼이 클릭되었어요.")
# btn7 = Button(root, text="동작하는 버튼", command=btncmd)
# btn7.pack()

# root.mainloop()

##############################
## 03. label
# from tkinter import *
# import os

# root = Tk()
# root.title("pGUI")
# root.geometry("640x480")

# label1 = Label(root, text="안녕하세요")
# label1.pack()

# curr_dir_path = os.path.dirname(os.path.abspath(__file__))
# file_path = curr_dir_path + '/userlib_pic/check.png'
# photo = PhotoImage(file=file_path)
# label2 = Label(root, image=photo)
# label2.pack()

# def change():
#     label1.config(text="또 만나요")
#     file_path = curr_dir_path + '/userlib_pic/axe.png'
#     global photo2 
#     photo2 = PhotoImage(file=file_path)
#     label2.config(image=photo2)

# btn = Button(root, text="클릭", command=change)
# btn.pack()

# root.mainloop()

##############################
## 04. text and entry
# from tkinter import *

# root = Tk()
# root.title("pGUI")
# root.geometry("640x480")

# txt = Text(root, width=30, height=5)
# txt.pack()
# txt.insert(END, "글자를 입력하세요")

# ee = Entry(root, width=30) # 한 줄 입력 받을 때
# ee.pack()
# ee.insert(0, "한 줄만 입력해요")

# def btncmd():
#     print(txt.get("1.0", END)) # 1: 첫 번째 라인, 0: 0번째 Coloumn 위치
#     print(ee.get())

#     txt.delete("1.0", END)
#     ee.delete(0, END)

# btn = Button(root, text="클릭", command=btncmd)
# btn.pack()

# root.mainloop()

##############################
## 05. list box
# from tkinter import *
# root = Tk()
# root.title("pGUI")
# root.geometry("640x480")

# listbox = Listbox(root, selectmode="extended", height=0)
# # listbox = Listbox(root, selectmode="extended", height=3)
# # listbox = Listbox(root, selectmode="single", height=0)
# listbox.insert(0, "사과")
# listbox.insert(1, "딸기")
# listbox.insert(2, "바나나")
# listbox.insert(END, "수박")
# listbox.insert(END, "포도")
# listbox.pack()

# def btncmd():
#     # listbox.delete(END)
#     # listbox.delete(0)
#     # print("리스트에는", listbox.size(), "개가 있어요")
#     # print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))
#     print("선택된 항목 : ", listbox.curselection())

# btn = Button(root, text="클릭", command=btncmd)
# btn.pack()

# root.mainloop()

##############################
## 06. Check button
# from tkinter import *
# root = Tk()
# root.title("pGUI")
# root.geometry("640x480")

# chkvar = IntVar() # int형 값 저장
# chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# # chkbox.select() # 자동 선택 처리
# # chkbox.deselect() # 선택 해제 처리
# chkbox.pack()

# chkvar2 = IntVar()
# chkbox2 = Checkbutton(root, text="일주일 동안 보지 않기", variable=chkvar2)
# chkbox2.pack()

# def btncmd():
#     print(chkvar.get())
#     print(chkvar2.get())

# btn = Button(root, text="클릭", command=btncmd)
# btn.pack()

# root.mainloop()

##############################
## 07. Radio button
# from tkinter import *
# root = Tk()
# root.title("pGUI")
# root.geometry("640x480")

# Label(root, text="메뉴를 선택하세요").pack()

# burger_var = IntVar()
# btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
# btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
# btn_burger3 = Radiobutton(root, text="치킨버거", value=3, variable=burger_var)

# btn_burger1.select()

# btn_burger1.pack()
# btn_burger2.pack()
# btn_burger3.pack()

# Label(root, text="음료를 선택하세요").pack()
# drink_var = StringVar()
# btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
# btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
# btn_drink1.select()
# btn_drink1.pack()
# btn_drink2.pack()

# def btncmd():
#     print(burger_var.get())
#     print(drink_var.get())

# btn = Button(root, text="주문", command=btncmd)
# btn.pack()

# root.mainloop()

##############################
## 08. Combo box
# import tkinter.ttk as ttk
# from tkinter import *
# root = Tk()
# root.title("pGUI")
# root.geometry("640x480")

# vals = [str(i) + "일" for i in range(1, 32)]
# combobox = ttk.Combobox(root, height=5, values=vals)
# combobox.pack()
# combobox.set("카드 결제일")

# readonly_combobox = ttk.Combobox(root, height=10, values=vals, state="readonly")
# readonly_combobox.current(0)
# readonly_combobox.pack()

# def btncmd():
#     print(combobox.get())
#     print(readonly_combobox.get())

# btn = Button(root, text="선택", command=btncmd)
# btn.pack()

# root.mainloop()

##############################
## 09. progress bar
# import tkinter.ttk as ttk
# from tkinter import *
# import time

# root = Tk()
# root.title("pGUI")
# root.geometry("640x480")

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar.start(10) # ms
# progressbar.pack()

# progressbar2 = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar2.start(10) # ms
# progressbar2.pack()

# p_var3 = DoubleVar()
# progressbar3 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var3)
# progressbar3.pack()

# def btncmd():
#     progressbar.stop()
#     progressbar2.stop()

# def btncmd2():
#     for i in range(1, 101):
#         time.sleep(0.01)
#         p_var3.set(i)
#         progressbar3.update()
#         print(p_var3.get())

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

# btn2 = Button(root, text="시작", command=btncmd2)
# btn2.pack()

# root.mainloop()

##############################
## 10. menu
# from tkinter import *

# root = Tk()
# root.title("pGUI")
# root.geometry("640x480")

# def create_new_file():
#     print("새 파일을 만듭니다.")

# # File menu
# menu = Menu(root)
# menu_file = Menu(menu, tearoff=0)
# menu_file.add_command(label="New File", command=create_new_file)
# menu_file.add_command(label="New Window")
# menu_file.add_separator()
# menu_file.add_command(label="Open File..")
# menu_file.add_separator()
# menu_file.add_command(label="Save all", state="disable")
# menu_file.add_separator()
# menu_file.add_command(label="Exit", command=root.quit)
# menu.add_cascade(label="File", menu=menu_file)

# # Edit menu
# menu.add_cascade(label="Edit")

# # Language menu (radio button)
# menu_lang = Menu(menu, tearoff=0)
# menu_lang.add_radiobutton(label="Python")
# menu_lang.add_radiobutton(label="Jave")
# menu_lang.add_radiobutton(label="C++")
# menu.add_cascade(label="Language", menu=menu_lang)

# # View menu (check box)
# menu_view = Menu(menu, tearoff=0)
# menu_view.add_checkbutton(label="Show minimap")
# menu.add_cascade(label="View", menu=menu_view)

# root.config(menu=menu)
# root.mainloop()

##############################
## 11. message box
# import tkinter.messagebox as msgbox
# from tkinter import *

# root = Tk()
# root.title("pGUI")
# root.geometry("640x480")

# def info():
#     msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")

# def warn():
#     msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")

# def error():
#     msgbox.showerror("에러", "결제 오류가 발생했습니다.")

# def okcancel():
#     msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매 하시겠습니까?")

# def retrycancel():
#     response = msgbox.askretrycancel("재시도 / 취소")
#     if response == True: # 1, True
#         print("재시도")
#     elif response == False: # 0, False
#         print("취소")
#     else:
#         pass

# def yesno():
#     msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")

# def yesnocancel():
#     response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다\n저장 후 프로그램을 종료하시겠습니까?")
#     if response == True: # 1, True
#         print("예")
#     elif response == False: # 0, False
#         print("아니오")
#     else:
#         print("취소")

# Button(root, command=info, text="알림").pack()
# Button(root, command=warn, text="경고").pack()
# Button(root, command=error, text="에러").pack()
# Button(root, command=okcancel, text="확인 취소").pack()
# Button(root, command=retrycancel, text="재시도 취소").pack()
# Button(root, command=yesno, text="예 아니오").pack()
# Button(root, command=yesnocancel, text="예 아니오 취소").pack()

# root.mainloop()

##############################
## 12. frame
# from tkinter import *

# root = Tk()
# root.title("pGUI")
# root.geometry("640x480")

# Label(root, text="메뉴를 선택해주세요").pack(side="top")
# Button(root, text="주문하기").pack(side="bottom")

# frame_burger = Frame(root, relief="solid", bd=1)
# frame_burger.pack(side="left", fill="both", expand=True)
# Button(frame_burger, text="햄버거").pack()
# Button(frame_burger, text="치즈버거").pack()
# Button(frame_burger, text="치킨버거").pack()

# frame_drink = LabelFrame(root, text="음료")
# frame_drink.pack(side="right", fill="both", expand=True)
# Button(frame_drink, text="콜라").pack()
# Button(frame_drink, text="사이다").pack()

# root.mainloop()

##############################
## 13. scroll bar
# from tkinter import *

# root = Tk()
# root.title("pGUI")
# root.geometry("640x480")

# frame = Frame(root)
# frame.pack()

# scrollbar = Scrollbar(frame)
# scrollbar.pack(side="right", fill="y")

# # listbox = Listbox(frame, selectmode="extended", height=10)
# listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
# for i in range(1, 31):
#     listbox.insert(END, str(i) + "일")
# listbox.pack(side="left")

# scrollbar.config(command=listbox.yview)
# root.mainloop()

##############################
## 14. grid
# ┌──────┬──────┬──────┬─────┐
# │ 0, 0 │ 0, 1 │ 0, 2 │ 0, 3│
# ├──────┼──────┼──────┼─────┤
# │ 1, 0 │ 1, 1 │ 1, 2 │ 1, 3│
# ├──────┼──────┼──────┼─────┤
# │ 2, 0 │ 2, 1 │ 2, 2 │ 2, 3│
# └──────┴──────┴──────┴─────┘

# from tkinter import *

# root = Tk()
# root.title("pGUI")
# root.geometry("640x480")

# btn1 = Button(root, text="버튼1")
# btn2 = Button(root, text="버튼2")

# # btn1.pack(side="left")
# # btn2.pack(side="left")
# btn1.grid(row = 0, column=0)
# btn2.grid(row = 1, column=1)

# root.mainloop()

##############################
## ex calculater
# from tkinter import *

# root = Tk()
# root.title("pGUI")
# root.geometry("640x480")

# # btn_f16 = Button(root, text="F16")
# # btn_f16 = Button(root, text="F16", padx=10, pady=10)
# btn_f16 = Button(root, text="F16", width=6, height=2)
# btn_f17 = Button(root, text="F17", width=6, height=2)
# btn_f18 = Button(root, text="F18", width=6, height=2)
# btn_f19 = Button(root, text="F19", width=6, height=2)
# # btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
# btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
# btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
# btn_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
# btn_f19.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

# btn_clear = Button(root, text="clear", width=6, height=2)
# btn_equal = Button(root, text="=", width=6, height=2)
# btn_div = Button(root, text="/", width=6, height=2)
# btn_mul = Button(root, text="*", width=6, height=2)
# btn_clear.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
# btn_equal.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
# btn_div.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
# btn_mul.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

# btn_7 = Button(root, text="7", width=6, height=2)
# btn_8 = Button(root, text="8", width=6, height=2)
# btn_9 = Button(root, text="9", width=6, height=2)
# btn_sub = Button(root, text="-", width=6, height=2)
# btn_7.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
# btn_8.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
# btn_9.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
# btn_sub.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)

# btn_4 = Button(root, text="4", width=6, height=2)
# btn_5 = Button(root, text="5", width=6, height=2)
# btn_6 = Button(root, text="6", width=6, height=2)
# btn_add = Button(root, text="+", width=6, height=2)
# btn_4.grid(row=3, column=0, sticky=W, padx=3, pady=3)
# btn_5.grid(row=3, column=1, sticky=W+S, padx=3, pady=3)
# btn_6.grid(row=3, column=2, sticky=E, padx=3, pady=3)
# btn_add.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)

# btn_1 = Button(root, text="1", width=6, height=2)
# btn_2 = Button(root, text="2", width=6, height=2)
# btn_3 = Button(root, text="3", width=6, height=2)
# btn_enter = Button(root, text="Enter", width=6, height=2)
# btn_1.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
# btn_2.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
# btn_3.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
# btn_enter.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3)

# btn_0 = Button(root, text="0", width=6, height=2)
# btn_point = Button(root, text=".", width=6, height=2)
# btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3)
# btn_point.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)

# root.mainloop()